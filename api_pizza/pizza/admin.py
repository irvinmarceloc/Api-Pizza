from django.contrib import admin
from pizza.models import *

##Para que el usuario pueda administrar las tablas desde el panel

#Administrar Pizzas
class PizzaAdmin(admin.ModelAdmin):
    list_display=("nombre", "precio", "activo") #Para ver con formatos
    search_fields=("nombre","activo") #Para filtrar por buscador

admin.site.register(Pizza, PizzaAdmin)
