from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import PerfilUsuario

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    """Crea un PerfilUsuario automáticamente cuando se crea un nuevo User."""
    if created:
        PerfilUsuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    """Guarda el perfil cuando se actualiza el User."""
    try:
        instance.perfilusuario.save()
    except PerfilUsuario.DoesNotExist:
        PerfilUsuario.objects.create(user=instance)
