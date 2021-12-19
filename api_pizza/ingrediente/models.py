from django.db import models

#Modelo Ingrediente
class Ingrediente(models.Model):
    nombre=models.CharField(primary_key=True, max_length=30)

    def __str__(self):
        return self.nombre