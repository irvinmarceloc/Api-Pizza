from django.db import models
from ingrediente.models import Ingrediente

#Modelo de piza
class Pizza(models.Model):
    id= models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    precio=models.IntegerField()
    activo=models.BooleanField()
    ingredientes = models.ManyToManyField(Ingrediente)

    
    def __str__(self):
        return self.nombre


##Relacionamos Pizza e Ingrediente mucho a mucho 