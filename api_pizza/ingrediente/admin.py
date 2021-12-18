from django.contrib import admin
from ingrediente.models import *
##Para que el usuario pueda administrar las tablas desde el panel

class IngredienteAdmin(admin.ModelAdmin):
    list_display=("nombre",) #Para ver con formatos

admin.site.register(Ingrediente, IngredienteAdmin)