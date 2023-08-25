from django import forms
from .models import Solicitudes, Adjuntos, Respuestas, Usuario

class AdjuntosForm(forms.ModelForm):
    class Meta:
        model = Adjuntos
        fields = ['archivo']

#Clase Solicitud, para capturar la información de la solicitud a enviar, por parte del ciudadano
class SolicitudForm(forms.ModelForm): 
    class Meta:
        model = Solicitudes  #Referencia al modelo Solicitudes en models.py, para enviar la información a la base de datos
        fields = ['titulo', 'lista_desplegable', 'fecha_reporte', 'descripcion']

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo') #Título de la solicitud, siendo una breve descripción del problema a reportar
        lista_desplegable = cleaned_data.get('lista_desplegable') #Define si es solicitud o reporte
        fecha_reporte = cleaned_data.get('fecha_reporte') #Campo capturado automáticamente, para fines de medir efectividad de la respuesta del funcionario de gobierno
        descripcion = cleaned_data.get('descripcion') #Descripción de la solicitud o reporte, donde se muestra a detalle la petición del ciudadano
        adjuntos = cleaned_data.get('adjuntos') #Archivos adjuntos, como fotografías o documentos, para fines de evidencia o agilidar de respuesta

        if not titulo or not fecha_reporte or not descripcion:
            raise forms.ValidationError('Todos los campos deben estar completos')
        
        return cleaned_data

#Forma de respuesta, donde el funcionario puede describir las acciones realizadas para conformidad del ciudadano
class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuestas  #Referencia al modelo respuestas en models.py, para enviar la información a la base de datos
        fields = ['fecha_respuesta', 'respuesta_servidor']

#Formulario de uso exclusivo del administrador, para creación de usuarios nuevos que puedan responder a solicitudes
class CrearUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario #Referencia al modelo Usuario en models.py, para enviar la información a la base de datos
        fields = ['nombre', 'email', 'contraseña'] #Información requerida en el formulario ,para almacenarla en auth_user de la base de datos.