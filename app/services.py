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

TOKEN_FILE        = os.path.join(settings.BASE_DIR, "padron_token_cache.json")
CERT_FILE         = settings.AFIP_CERT_FILE
KEY_FILE          = settings.AFIP_KEY_FILE
CUIT_REPRESENTADA = settings.AFIP_CUIT_REPRESENTADA

def obtener_token_sign():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE) as f:
            cache = json.load(f)
        expira = datetime.datetime.fromisoformat(cache["expiration"])
        if datetime.datetime.now() < expira - datetime.timedelta(minutes=5):
            return cache["token"], cache["sign"]

    with open(CERT_FILE, "rb") as f:
        cert = x509.load_pem_x509_certificate(f.read())
    with open(KEY_FILE, "rb") as f:
        key = serialization.load_pem_private_key(f.read(), password=None)

    now        = datetime.datetime.now()
    expiration = now + datetime.timedelta(hours=10)

    tra_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<loginTicketRequest version="1.0">
  <header>
    <uniqueId>{int(now.timestamp())}</uniqueId>
    <generationTime>{(now - datetime.timedelta(minutes=10)).strftime('%Y-%m-%dT%H:%M:%S')}</generationTime>
    <expirationTime>{expiration.strftime('%Y-%m-%dT%H:%M:%S')}</expirationTime>
  </header>
  <service>ws_sr_padron_a13</service>
</loginTicketRequest>""".encode("utf-8")

    signature = (
        pkcs7.PKCS7SignatureBuilder()
        .set_data(tra_xml)
        .add_signer(cert, key, hashes.SHA256())
        .sign(serialization.Encoding.DER, options=[])
    )

    cms_base64   = base64.b64encode(signature).decode()
    client       = Client("https://wsaa.afip.gov.ar/ws/services/LoginCms?wsdl")
    response_xml = client.service.loginCms(cms_base64)
    xml_obj      = etree.fromstring(response_xml.encode("utf-8"))
    token        = xml_obj.find(".//token").text
    sign         = xml_obj.find(".//sign").text

    with open(TOKEN_FILE, "w") as f:
        json.dump({"token": token, "sign": sign, "expiration": expiration.isoformat()}, f)

    return token, sign

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
        token, sign = obtener_token_sign()
        client = Client("https://aws.afip.gov.ar/sr-padron/webservices/personaServiceA13?wsdl")
        response = client.service.getPersona(
            token=token,
            sign=sign,
            cuitRepresentada=CUIT_REPRESENTADA,
            idPersona=int(cuit)
        )
        data       = serialize_object(response)
        persona    = data.get("persona") or {}
        domicilios = persona.get("domicilio") or []

        dir_fiscal, prov_fiscal, loc_fiscal = get_domicilio(domicilios, "FISCAL")
        dir_legal,  prov_legal,  loc_legal  = get_domicilio(domicilios, "LEGAL/REAL")

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
        return {"cuit": cuit, "error": str(e)}