from ast import Delete
from django.db import models

# Create your models here.

class Datos(models.Model):
    ID=models.CharField(primary_key=True, max_length=6)
    Nombre=models.CharField(verbose_name="Nombre",max_length=50)
    Apellido=models.CharField(verbose_name="Apellido",max_length=50)
    Correo=models.CharField(verbose_name="correo", max_length=50)

    def __str__(self):
        texto = "{0}, {1}, {2}"
        return texto.format("ID: " + self.ID, "Nombre: " + self.Nombre, "Apellido: " + self.Apellido, "Correo: " + self.Correo)

    
        
   
