from django.contrib import admin
from ingrediente.models import *

##Para que el usuario pueda administrar las tablas desde el panel

class IngredienteAdmin(admin.ModelAdmin):
    list_display=("nombre", "id") #Para ver con formatos
    nombre=models.CharField(max_length=30)
    id =models.BooleanField()

admin.site.register(Ingrediente, IngredienteAdmin)