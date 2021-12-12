from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all() 
    serializers_class = UsuarioSerializer

