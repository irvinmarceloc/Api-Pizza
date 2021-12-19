from django.contrib import admin
from ingrediente.models import *
##Para que el usuario pueda administrar las tablas desde el panel

admin.site.register(Ingrediente)