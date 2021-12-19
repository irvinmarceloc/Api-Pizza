# Django REST Framework
from rest_framework import serializers
# Model
from ingrediente.models import Ingrediente

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = [
            'nombre',
        ]