import datetime
import base64
import json
import os
from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.serialization import pkcs7
from zeep import Client
from zeep.helpers import serialize_object
from lxml import etree
from django.conf import settings
from pathlib import Path
import tempfile
import logging

# Configuramos el logger para que use el canal de errores de gunicorn
logger = logging.getLogger('gunicorn.error')
TOKEN_FILE = settings.BASE_DIR /"certs/padron_token_cache.json"
CERT_FILE         = settings.AFIP_CERT_FILE
KEY_FILE          = settings.AFIP_KEY_FILE
CUIT_REPRESENTADA = settings.AFIP_CUIT_REPRESENTADA

def obtener_token_sign():
    logger.info(">>> [WSAA] Iniciando proceso de obtención de Token/Sign...")

    # 1. Intento de recuperación desde el archivo caché
    if os.path.exists(TOKEN_FILE):
        logger.info(f">>> [WSAA] Buscando caché en {TOKEN_FILE}")
        try:
            with open(TOKEN_FILE, "r") as f:
                cache = json.load(f)
            
            expira = datetime.datetime.fromisoformat(cache["expiration"])
            # Si el token es válido por al menos 5 minutos más, lo usamos
            if datetime.datetime.now() < expira - datetime.timedelta(minutes=5):
                logger.info(">>> [WSAA] Token válido recuperado del caché local.")
                return cache["token"], cache["sign"]
            else:
                logger.warning(">>> [WSAA] El token en caché ha expirado o está por expirar. Solicitando uno nuevo...")
        except (json.JSONDecodeError, KeyError, ValueError, OSError) as e:
            logger.error(f">>> [WSAA] Error al leer el archivo de caché ({type(e).__name__}): {e}")
            # Continuamos para pedir uno nuevo si el caché falla
            pass

    # 2. Si no hay caché válido, solicitar nuevo a la AFIP
    try:
        logger.info(">>> [WSAA] Cargando certificados y clave privada...")
        with open(CERT_FILE, "rb") as f:
            cert = x509.load_pem_x509_certificate(f.read())
        with open(KEY_FILE, "rb") as f:
            key = serialization.load_pem_private_key(f.read(), password=None)

        now = datetime.datetime.now()

    # AFIP es sensible. Restamos solo 1 minuto para asegurar que no sea 'el futuro'
    # pero que tampoco sea muy viejo.
        generation_time = now - datetime.timedelta(minutes=1)
        expiration_time = now + datetime.timedelta(hours=12)

        tra_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
        <loginTicketRequest version="1.0">
        <header>
        <uniqueId>{int(now.timestamp())}</uniqueId>
        <generationTime>{generation_time.strftime('%Y-%m-%dT%H:%M:%S')}</generationTime>
        <expirationTime>{expiration_time.strftime('%Y-%m-%dT%H:%M:%S')}</expirationTime>
        </header>
        <service>ws_sr_padron_a13</service>
        </loginTicketRequest>""".strip().encode("utf-8")

        # Firma PKCS#7
        logger.info(">>> [WSAA] Firmando el TRA (CMS)...")
        signature = (
            pkcs7.PKCS7SignatureBuilder()
            .set_data(tra_xml)
            .add_signer(cert, key, hashes.SHA256())
            .sign(serialization.Encoding.DER, options=[])
        )

        cms_base64 = base64.b64encode(signature).decode()
        
        # Llamada al WSAA (Punto de falla común por red/VPN)
        url_wsaa = "https://wsaa.afip.gov.ar/ws/services/LoginCms?wsdl"
        logger.info(f">>> [WSAA] Conectando a {url_wsaa}...")
        
        client = Client(url_wsaa)
        response_xml = client.service.loginCms(cms_base64)
        
        logger.info(">>> [WSAA] Respuesta recibida exitosamente de AFIP.")
        
        xml_obj = etree.fromstring(response_xml.encode("utf-8"))
        token = xml_obj.find(".//token").text
        sign = xml_obj.find(".//sign").text

        # 3. Intentar guardar en el archivo caché
        try:
            logger.info(f">>> [WSAA] Intentando guardar nuevo token en {TOKEN_FILE}")
            # Asegurarse de que el directorio existe
            os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
            with open(TOKEN_FILE, "w") as f:
                json.dump({
                    "token": token, 
                    "sign": sign, 
                    "expiration": expiration.isoformat()
                }, f)
            logger.info(">>> [WSAA] Token guardado en caché exitosamente.")
        except Exception as e:
            logger.error(f">>> [WSAA] ERROR AL GUARDAR CACHÉ: {e}") 
            # No retornamos error aquí para que la app siga funcionando aunque no pueda guardar el caché
        
        return token, sign

    except Exception as e:
        logger.exception(f">>> [WSAA] ERROR CRÍTICO en la obtención del ticket: {str(e)}")
        raise e

def get_domicilio(domicilios, tipo):
    for d in (domicilios or []):
        if d.get("tipoDomicilio", "").upper() == tipo.upper():
            return (
                d.get("direccion") or "",
                d.get("descripcionProvincia") or "",
                d.get("localidad") or ""
            )
    return ("", "", "")

def consultar_cuit(cuit):
    try:
        logger.info(f">>> [AFIP] Iniciando consulta para CUIT: {cuit}")
        
        # 1. Obtención de credenciales
        try:
            token, sign = obtener_token_sign()
            logger.debug(">>> [AFIP] Token y Sign obtenidos correctamente.")
        except Exception as e:
            logger.error(f">>> [AFIP] Error crítico obteniendo Token/Sign: {str(e)}")
            return {"cuit": cuit, "error": f"Error de autenticación: {str(e)}"}

        # 2. Conexión al Web Service de Padrón A13
        logger.info(">>> [AFIP] Conectando a personaServiceA13...")
        client = Client("https://aws.afip.gov.ar/sr-padron/webservices/personaServiceA13?wsdl")
        
        response = client.service.getPersona(
            token=token,
            sign=sign,
            cuitRepresentada=CUIT_REPRESENTADA,
            idPersona=int(cuit)
        )
        
        # 3. Procesamiento de la respuesta
        data = serialize_object(response)
        logger.debug(f">>> [AFIP] Respuesta serializada: {data}")

        persona = data.get("persona") or {}
        if not persona:
            logger.warning(f">>> [AFIP] No se encontró información para el CUIT {cuit}. Respuesta vacía.")
            return {"cuit": cuit, "error": "No se encontró la persona"}

        domicilios = persona.get("domicilio") or []

        dir_fiscal, prov_fiscal, loc_fiscal = get_domicilio(domicilios, "FISCAL")
        dir_legal,  prov_legal,  loc_legal  = get_domicilio(domicilios, "LEGAL/REAL")

        logger.info(f">>> [AFIP] Consulta exitosa para {persona.get('razonSocial', 'Sin Nombre')}")

        return {
            "cuit":             cuit,
            "dni":              persona.get("numeroDocumento") or "",
            "apellido":         persona.get("apellido") or "",
            "nombre":           persona.get("nombre") or "",
            "razon_social":     persona.get("razonSocial") or "",
            "tipo_persona":     persona.get("tipoPersona") or "",
            "actividad":        persona.get("descripcionActividadPrincipal") or "",
            "domicilio_fiscal": dir_fiscal,
            "provincia_fiscal": prov_fiscal,
            "localidad_fiscal": loc_fiscal,
            "domicilio_legal":  dir_legal,
            "provincia_legal":  prov_legal,
            "localidad_legal":  loc_legal,
            "error":            ""
        }

    except Exception as e:
        # El logger.exception captura el traceback completo (muy útil para debuguear)
        logger.exception(f">>> [AFIP] ERROR NO CONTROLADO consultando CUIT {cuit}: {str(e)}")
        return {"cuit": cuit, "error": str(e)}