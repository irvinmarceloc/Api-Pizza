# Django REST Framework
from rest_framework import serializers
# Model
from ingrediente.models import Ingrediente

class IngredienteModelSerializer(serializers.ModelSerializer):
    """Ingrediente Model Serializer"""

    class Meta:
        """Meta class."""

        model = Ingrediente
        fields = (
            'nombre',
        )

class IngredienteSerializer(serializers.Serializer):
    nombre= serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, data):

        exp = Ingrediente.objects.create(**data)
        return exp