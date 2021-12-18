from django.db import models

#Modelo Ingrediente
class Ingrediente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    
