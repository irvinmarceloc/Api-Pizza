from rest_framework import serializers, viewsets
from rest_framework.response import Response

from pizza.models import Pizza
from ingrediente.models import Ingrediente

from .serializers import PizzaSerializer
from ingrediente.serializers import IngredienteSerializer

from django.shortcuts import render

# Create your views here.

class PizzaViewSet(viewsets.ModelViewSet):
    serializer_class = PizzaSerializer

    def get_queryset(self):
        pizza = Pizza.objects.all()
        return pizza

    
    def create(self, request, *args, **kwargs):
        
        data = request.data 
        
        new_pizza = Pizza.objects.create(id=data["id"], nombre=data["nombre"], precio=data["precio"],activo=data["activo"] ) 
        
        new_pizza.save()

        for ingrediente in data["ingredientes"]:
            ingrediente_obj = Ingrediente.objects.get(nombre=ingrediente["nombre"])
            new_pizza.ingredientes.add(ingrediente_obj)
        
        serializer = PizzaSerializer(new_pizza)

        return Response(serializer.data)

class IngredienteViewSet(viewsets.ModelViewSet):
    serializers_class = IngredienteSerializer

    def get_queryset(self):
        ingrediente = Ingrediente.objects.all()
        return ingrediente 