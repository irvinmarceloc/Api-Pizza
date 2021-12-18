from rest_framework import viewsets
from rest_framework.response import Response

from pizza.models import Pizza
#from ingrediente.models import Ingrediente

from .serializers import PizzaModelSerializer, PizzaSerializer
#from ingrediente.serializers import IngredienteModelSerializer

from django.shortcuts import render

# Create your views here.

class PizzaViewSet(viewsets.ModelViewSet):
    serializer_class = PizzaSerializer

    def get_queryset(self):
        pizza = Pizza.objects.all()
        return pizza