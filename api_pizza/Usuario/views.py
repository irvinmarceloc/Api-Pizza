from django.shortcuts import render
from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioList(generics.ListCreateAPIView):
    

