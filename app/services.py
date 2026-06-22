import datetime
import base64
import json
import os
import smtplib
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
from django.utils import timezone
import pytz
import requests
import smtplib
from email.mime.text import MIMEText
from django.core.management.base import BaseCommand
from django.conf import settings
import logging
from django.conf import settings
from django.core.mail import send_mail

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
        try:
            with open(TOKEN_FILE, "r") as f:
                cache = json.load(f)
            
            # Hacer que la comparación sea "timezone aware"
            expira = datetime.datetime.fromisoformat(cache["expiration"])
            if datetime.datetime.now(pytz.utc) < expira - datetime.timedelta(minutes=5):
                logger.info(">>> [WSAA] Token válido recuperado del caché local.")
                return cache["token"], cache["sign"]
        except Exception as e:
            logger.error(f">>> [WSAA] Error al leer caché: {e}")
            pass

    # 2. Solicitar nuevo a la AFIP
    try:
        # Forzamos la zona horaria de Argentina (UTC-3)
        tz_ar = pytz.timezone('America/Argentina/Buenos_Aires')
        now_ar = datetime.datetime.now(tz_ar)

        # AFIP es estricta: restamos 2 minutos para asegurar que para ellos NO sea el futuro
        # IMPORTANTE: Reemplazamos microsegundos a 0 para evitar errores de parseo en AFIP
        # Cambia el desfase de -2 minutos a -10 minutos
        generation_time = (now_ar - datetime.timedelta(minutes=10)).replace(microsecond=0)

        # Asegúrate de mantener la expiración en un rango normal (ej: 2 horas adelante de la actual)
        expiration_time = (now_ar + datetime.timedelta(hours=2)).replace(microsecond=0) # 2 horas es el estándar recomendado

        # Formatear con Offset de Zona Horaria (ej: 2026-06-22T10:35:22-03:00)
        # Reemplazamos el %z final de Python (ej: -0300) por el formato ISO requerido (-03:00)
        gen_str = generation_time.strftime('%Y-%m-%dT%H:%M:%S%z')
        gen_str = gen_str[:-2] + ":" + gen_str[-2:]
        
        exp_str = expiration_time.strftime('%Y-%m-%dT%H:%M:%S%z')
        exp_str = exp_str[:-2] + ":" + exp_str[-2:]

        # --- CONTROL DE LOGS EXPLICITO ---
        logger.info("================ [MONITORAFIP] ================")
        logger.info(f"Hora actual AR:  {now_ar.isoformat()}")
        logger.info(f"generationTime:  {gen_str}")
        logger.info(f"expirationTime:  {exp_str}")
        logger.info(f"Unique ID (TS):  {int(now_ar.timestamp())}")
        logger.info("===============================================")

        # IMPORTANTE: XML sin indentación a la izquierda (pegado al borde)
        tra_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<loginTicketRequest version="1.0">
<header>
<uniqueId>{int(now_ar.timestamp())}</uniqueId>
<generationTime>{gen_str}</generationTime>
<expirationTime>{exp_str}</expirationTime>
</header>
<service>ws_sr_padron_a13</service>
</loginTicketRequest>""".strip().encode("utf-8")

        # --- Resto de tu lógica de firma (Carga de certs, PKCS7, etc.) ---
        with open(CERT_FILE, "rb") as f:
            cert = x509.load_pem_x509_certificate(f.read())
        with open(KEY_FILE, "rb") as f:
            key = serialization.load_pem_private_key(f.read(), password=None)

        signature = (
            pkcs7.PKCS7SignatureBuilder()
            .set_data(tra_xml)
            .add_signer(cert, key, hashes.SHA256())
            .sign(serialization.Encoding.DER, options=[])
        )

        cms_base64 = base64.b64encode(signature).decode()
        client = Client("https://wsaa.afip.gov.ar/ws/services/LoginCms?wsdl")
        
        # Intentar llamada al WS controlando la respuesta exacta
        try:
            response_xml = client.service.loginCms(cms_base64)
        except Exception as ws_err:
            logger.error(f">>> [WSAA] Error directo en la llamada SOAP a AFIP: {ws_err}")
            raise ws_err

        xml_obj = etree.fromstring(response_xml.encode("utf-8"))
        token = xml_obj.find(".//token").text
        sign = xml_obj.find(".//sign").text

        # 3. Guardar en caché (Guardamos en ISO con zona horaria)
        try:
            os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
            with open(TOKEN_FILE, "w") as f:
                json.dump({
                    "token": token, 
                    "sign": sign, 
                    "expiration": expiration_time.isoformat()
                }, f)
        except Exception as e:
            logger.error(f">>> [WSAA] No se pudo guardar caché: {e}")
        
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
    
def verificar_conexion_datacenter(termino="10245"):
    url_interna = f"http://192.168.0.233/expediente/deuda/?numero={termino}"
    
    try:
        logger.info(f"📡 Enviando petición a {url_interna} (Timeout=5s)...")
        response = requests.get(url_interna, timeout=5)
        
        # Si el estado es 4xx o 5xx, lanza HTTPError
        response.raise_for_status() 
        
        try:
            data = response.json()
            logger.info(f"✅ Conexión y JSON validados con el Datacenter. Status {response.status_code}")
            return True, data
        except (ValueError, requests.exceptions.JSONDecodeError) as json_err:
            error_format = f"El Datacenter respondió 200 OK pero el contenido NO es un JSON válido. Respuesta: {response.text[:300]}"
            logger.error(f"🔴 ERROR DE FORMATO: {error_format}")
            enviar_alerta_email(error_format, tipo_falla="Respuesta JSON Inválida de la API")
            return False, "La respuesta del servidor central tiene un formato inválido."
        
    except requests.exceptions.HTTPError as http_err:
        status_code = response.status_code
        error_msg = f"Error HTTP {status_code} devuelto por el Datacenter. Respuesta: {response.text[:200]}"
        logger.error(f"🔴 ERROR EN APLICACIÓN: {error_msg}")
        enviar_alerta_email(error_msg, tipo_falla=f"Error en Servidor Central (HTTP {status_code})")
        return False, error_msg

    # 🛡️ BLOQUE BLINDADO: Atrapamos cualquier error de Timeout (Connect, Read) o de Conexión de requests
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, requests.exceptions.RequestException) as net_err:
        error_msg = str(net_err)
        logger.error(f"📶 ERROR DE CONEXIÓN O TIMEOUT (VPN CAÍDA): {error_msg}")
        
        # Disparamos el correo indicando la caída
        enviar_alerta_email(error_msg, tipo_falla="Caída de Conexión / VPN Inalcanzable (Timeout)")
        return False, error_msg


def enviar_alerta_email(error_msg, tipo_falla):
    """Despacha el correo dinámico detallando el tipo de falla."""
    asunto = f"⚠️ ALERTA CRÍTICA: {tipo_falla} - SIEMSa"
    cuerpo = f"""
    Se ha detectado una anomalía al intentar conectar con el Datacenter de la Provincia.
    
    Tipo de Incidente: {tipo_falla}
    URL Evaluada: http://192.168.0.233/expediente/deuda/
    
    Detalles técnicos del fallo:
    ---------------------------------------------------------
    {error_msg}
    ---------------------------------------------------------
    
    Monitoreo Automático - SIEMSa.
    """
    
    try:
        send_mail(
            subject=asunto,
            message=cuerpo,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["franciscruz991@gmail.com"],
            fail_silently=False,
        )
        logger.info("📧 Correo de alerta enviado con éxito vía Django Mail Backend.")
    except Exception as ex:
        logger.error(f"❌ Error crítico al intentar despachar el email de alerta: {str(ex)}")