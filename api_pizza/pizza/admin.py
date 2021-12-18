from django.contrib import admin
from django.db.models.base import Model
from pizza.models import *
from ingrediente.models import *


##Para que el usuario pueda administrar las tablas desde el panel
class pizzaingrediente(admin.ModelAdmin):
    pass

#Administrar Pizzas
class PizzaAdmin(admin.ModelAdmin):
    Model = Pizza
    filter_horizontal=("ingredientes",) #La union mucho a mucho



    
admin.site.register(Pizza, PizzaAdmin)
