from django.db import models
from datetime import datetime
from django.utils import timezone

# Opciones para el tipo de solicitud, si es reporte de problema o una solicitud de información
TIPO_SOLICITUD_CHOICES = [
    ('Reporte de problema', 'Reporte de problema'),
    ('Solicitud de información', 'Solicitud de información')
]

#Modelo utilizado para los adjuntos opcionales. Se separó por cuestiones del valor a retornar
class Adjuntos(models.Model):
    archivo = models.FileField(upload_to='adjuntos/', null=True) #Se almacenan en la carpeta adjuntos/

# Modelo que representa las solicitudes realizadas por el ciudadano
class Solicitudes(models.Model):
    class Meta:
        verbose_name = 'Solicitudes' #Se asigna el nombre en singular y plural, para evitar doble "S" en la tabla de SQL
        verbose_name_plural = 'Solicitudes'

    titulo = models.CharField("Título", max_length=300, default="Título de la solicitud a levantar") #Título de la solicitud, siendo una breve descripción
    lista_desplegable = models.CharField("Tipo de solicitud", max_length=50, choices=TIPO_SOLICITUD_CHOICES, default="Reporte de problema") #Si es reporte o solicitud de información
    fecha_reporte = models.DateField("Fecha del reporte",  default=datetime.today) #Se asigna el valor de la fecha actual, para fines de medición de respuesta por parte de los funcioanrios
    descripcion = models.CharField(max_length=500, default="Describa la solicitud a enviar") #información detallada del reporte o solicitud a levantar por el ciudadano
    adjuntos = models.OneToOneField(Adjuntos, on_delete=models.CASCADE, null=True, blank=True) #Archivos adjuntos opcionales, para agilizar la respuesta a la solicitud, y para fines de evidencia

    def __int__(self):
        return self.pk #Devuelve la llave primaria, para fines de relacionar tablas, y evitar crear modelos adicionales innecesarios
#Modelo que representa las respuestas de los servidores públicos
class Respuestas(models.Model):
    class Meta:
        verbose_name = 'Respuestas' #Se asigna el nombre en singular y plural, para evitar doble "S" en la tabla de SQL
        verbose_name_plural = 'Respuestas'

    solicitud = models.ForeignKey(Solicitudes, on_delete=models.CASCADE) #Llave primaria de la tabla Solicitudes, para ligar la respuesta del servidor
    fecha_respuesta = models.DateField("Fecha de respuesta", default=timezone.now) #Fecha actual, para fines de medición de la respuesta de funcionarios de gobierno
    respuesta_servidor = models.CharField("Contenido de la respuesta del servidor público", max_length=500, default="Escriba la respuesta a la solicitud") #respuesta a detalle del servidor público

    def __str__(self):
        return f"respuesta para la solicitud: { self.solicitud.pk }" #Texto a mostrar, para visualizar el registro siendo contestado
    
#Modelo a utilizar por el administrador, para la creación de nuevos usuarios que puedan responder solicitudes 
class Usuario(models.Model):
    class Meta:
        verbose_name = 'Usuario'  #Se asigna el nombre en singular y plural, para evitar doble "S" en la tabla de SQL
        verbose_name_plural = 'Usuario'

    nombre = models.CharField(max_length=100) #nombre del usuario, el cual debe usar para autenticarse
    email = models.EmailField(unique=True) #Correo, para fines de recuperación de contraseña, en caso de olvidarla
    fecha_creacion = models.DateTimeField(auto_now_add=True) #Fecha de la creación de usuario, enviada automáticamente sin necesidad de asignarle valor manualmente
    contraseña = models.CharField(max_length=100) #Contraseña del usuario, no es visible en phpadmin. Si se olvida, debe seguirse el proceso de recuperación.

    def __str__(self):
        return self.nombre #Devuelve el nombre del usuario