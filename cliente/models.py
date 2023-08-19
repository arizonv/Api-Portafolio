from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime
from servicio.models import Agenda
import random
import string
from django.core.mail import send_mail
from django.conf import settings
from .utils import generar_codigo, generar_qr, enviar_correo

class Cliente(models.Model):
    SEXO = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]
    user = models.OneToOneField(
        'accounts.User',
        verbose_name='Usuario',
        on_delete=models.CASCADE
    )
    rut = models.CharField(max_length=10)
    sexo = models.CharField(max_length=10, choices=SEXO)

    def __str__(self):
        return f'{self.user.username}'

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    dia = models.DateField()
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('pendiente', 'Pendiente'),
        ('finalizada', 'Finalizada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')

    class Meta:
        unique_together = ('agenda', 'cliente', 'dia')

    def __str__(self):
        formatted_date = self.dia.strftime('%d-%m-%Y')
        return f"Reserva de {self.cliente} para el {formatted_date}, {self.agenda.cancha} {self.agenda.horario}"


@receiver(post_save, sender=Reserva)
def crear_ticket(sender, instance, created, **kwargs):
    if created or (not instance._state.adding and instance.estado == 'pendiente'):
        existing_ticket = Ticket.objects.filter(reserva=instance).first()

        if not existing_ticket:
            codigo = generar_codigo()
            correo_destino = 'arizonatitulo23@gmail.com'
            cliente = instance.cliente
            detalles = instance.agenda
            asunto = 'Qr de verificación para tu reserva'
            mensaje = f'Tu código de seguridad: {codigo}'
            
            qr_data = {
                'codigo_seguro': codigo,
                'cliente_user': cliente.user.username,
                'cliente_nombre': cliente.user.name,
                'cliente_apellidos': cliente.user.apellidos,
                'cancha': str(detalles.cancha),
                'horario': str(detalles.horario),
                'dia': instance.dia.strftime('%d-%m-%Y'),  
                'estado': instance.estado,
            }
            qr_img = generar_qr(qr_data)
            enviar_correo(asunto, mensaje, correo_destino, qr_img)
            Ticket.objects.create(cliente=cliente, reserva=instance, codigo=codigo)


class Ticket(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)


class Boleta(models.Model):
    fecha_emision = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f'Boleta para {self.cliente} emitida el {self.fecha_emision}'
