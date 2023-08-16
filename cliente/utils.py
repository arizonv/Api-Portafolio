import uuid
import qrcode
from io import BytesIO
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


#FUNCIONES PARA EL ENVIO DEL CODIGO DE SEGURIDAD Y EL CODIGO QR

#CODIGO DE SEGURIDAD
def generar_codigo():
    return str(uuid.uuid4().hex)[:10]

#CODIGO QR
def generar_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img


#ENVIO DE CORREO
def enviar_correo(asunto, mensaje, correo_destino, qr_img):
    buffer = BytesIO()
    qr_img.save(buffer, format="PNG")
    buffer.seek(0)

    email = EmailMessage(asunto, mensaje, settings.EMAIL_HOST_USER, [correo_destino])
    email.attach('codigo_qr.png', buffer.getvalue(), 'image/png')
    email.send(fail_silently=False)
