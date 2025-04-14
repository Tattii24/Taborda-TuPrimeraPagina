from django.db import models

# Create your models here.
class Zapato(models.Model):
    marca= models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    talla=models.IntegerField()
    color=models.CharField(max_length=30, default='sin color')

    def __str__(self):
        return f'{self.marca}  {self.modelo} -Talla {self.talla} ({self.color})'
