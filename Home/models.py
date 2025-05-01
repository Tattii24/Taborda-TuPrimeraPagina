from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete

class Zapato(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    talla = models.CharField(max_length=10)
    color = models.CharField(max_length=50, default='sin color', blank=True)
    fecha_creacion = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='zapatos/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"

@receiver(pre_delete, sender=Zapato)
def delete_zapato_images(sender, instance, **kwargs):
    """Borra las imágenes cuando se elimina un zapato"""
    if instance.imagen:
        instance.imagen.delete(save=False)
