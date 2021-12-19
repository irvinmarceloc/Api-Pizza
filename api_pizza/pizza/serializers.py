# Django REST Framework
from rest_framework import serializers
# Model
from pizza.models import Pizza

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = [
            'nombre',
            'precio',
            'ingredientes',
            'activo'
        ]


