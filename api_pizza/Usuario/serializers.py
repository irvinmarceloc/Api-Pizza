from django.db.models import fields
from rest_framework import serializers 
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id',
            'nombre',
        )