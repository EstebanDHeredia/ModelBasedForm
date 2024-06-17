from django.db import models

options = [
    [0, 'Pedido de información'],
    [1, 'Queja por un producto'],
    [2, 'Felicitaciones']
]

# Create your models here.
class Contact (models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre y apellido")
    email = models.EmailField(verbose_name="Correo electrónico")
    message = models.TextField(verbose_name="Mensaje")
    contact_type = models.IntegerField(choices=options, verbose_name="Tipo de contacto")
    subscription = models.BooleanField(default=False, verbose_name="Suscribirme a correos informativos")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"