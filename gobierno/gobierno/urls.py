from django.contrib import admin
from django.urls import path, include   #Agregamos include, para incluir la lista de urls en la app

from . import views

urlpatterns = [
    path('admin/', admin.site.urls), #url de admin, para gestionar las tablas y usuarios
    path('solicitudes/', include("solicitudes.urls")), #hace referencia a nuestra aplicación solicitudes

]
