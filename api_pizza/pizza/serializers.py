# Django REST Framework
from rest_framework import serializers
# Model
from pizza.models import Pizza

class PizzaModelSerializer(serializers.ModelSerializer):
    """Pizza Model Serializer"""

    class Meta:
        """Meta class."""

        model = Pizza
        fields = (
            'id',
            'nombre',
            'precio',
            'activo'
        )

class PizzaSerializer(serializers.Serializer):

    id= serializers.IntegerField()
    nombre= serializers.HiddenField(default=serializers.CurrentUserDefault())
    precio= serializers.IntegerField()
    activo= serializers.BooleanField()

    def create(self, data):

        exp = Pizza.objects.create(**data)
        return exp