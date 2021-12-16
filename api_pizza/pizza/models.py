from django.db import models

#Modelo de piza
class Pizza(models.Model):
    nombre=models.CharField(max_length=30)
    precio=models.IntegerField()
    activo=models.BooleanField()

    def __str__(self):
        return self.nombre
        