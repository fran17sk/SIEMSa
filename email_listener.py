import imaplib
import email
import time
from datetime import datetime
import pytz
import django
import os

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Exportaciones.settings")
django.setup()

from django.core.mail import send_mail
from django.conf import settings

# Configuración IMAP Gmail
IMAP_HOST = "imap.gmail.com"
IMAP_USER = settings.EMAIL_HOST_USER
IMAP_PASS = settings.EMAIL_HOST_PASSWORD

TZ = pytz.timezone("America/Argentina/Salta")

def es_horario_auto():
    ahora = datetime.now(TZ)
    dia = ahora.weekday()  # 0 lunes, 6 domingo
    hora = ahora.hour

    # Sábado y domingo → auto
    if dia >= 5:
        return True

    # Lunes a viernes → fuera de 8 a 14 → auto
    if hora < 8 or hora >= 11:
        return True

    return False

def responder(destinatario):
    asunto = "Recepción de su consulta"
    mensaje = (
        "Le informamos que su consulta ha sido recibida.\n\n"
        "Será atendida dentro del horario laboral:\n"
        "Lunes a viernes de 08:00 a 14:00 hs.\n\n"
        f"{settings.ORGANISMO}"
    )

    send_mail(
        asunto,
        mensaje,
        settings.DEFAULT_FROM_EMAIL,
        [destinatario],
        fail_silently=False
    )

def escuchar_correo():
    mail = imaplib.IMAP4_SSL(IMAP_HOST)
    mail.login(IMAP_USER, IMAP_PASS)

    while True:
        print('Revisando....')
        mail.select("inbox")
        status, mensajes = mail.search(None, "UNSEEN")

        if status == "OK":
            for num in mensajes[0].split():
                status, datos = mail.fetch(num, "(RFC822)")
                msg = email.message_from_bytes(datos[0][1])
                
                remitente = email.utils.parseaddr(msg["From"])[1]

                if es_horario_auto():
                    responder(remitente)

        time.sleep(30)  # revisa cada 30 segundos


if __name__ == "__main__":
    escuchar_correo()