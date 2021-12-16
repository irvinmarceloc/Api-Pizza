from django.db import models

#Modelo Ingrediente
class Ingrediente(models.Model):
    nombre=models.CharField(max_length=30)
    categoria=models.BooleanField()