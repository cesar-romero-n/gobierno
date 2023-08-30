from rest_framework import serializers
from .models import Usuario, Solicitudes

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'fecha_creacion']

class SolicitudesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitudes
        fields = ['id', 'titulo', 'lista_desplegable', 'fecha_reporte', 'descripcion']