from django.db import models

#Modelo Ingrediente
class Ingrediente(models.Model):
    nombre=models.CharField(primary_key=True, max_length=30)
    
    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre