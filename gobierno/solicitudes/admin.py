from django.contrib import admin
from .models import Solicitudes, Respuestas

admin.site.register(Solicitudes) #Registro de modelos Solicitudes y Respuestas, para el panel de django
admin.site.register(Respuestas)
