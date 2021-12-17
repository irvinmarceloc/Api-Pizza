from django.db import models
from ingrediente.models import Ingrediente

#Modelo de piza
class Pizza(models.Model):
    nombre=models.CharField(max_length=30)
    ingredientes= models.ManyToManyField(Ingrediente)
    precio=models.IntegerField()
    activo=models.BooleanField()

    def __str__(self):
        return self.nombre

##Relacionamos Pizza e Ingrediente mucho a mucho 