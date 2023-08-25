from django.apps import AppConfig


class SolicitudesConfig(AppConfig): #SolicitudesConfig heredando la clase AppConfig para configurar la app de solicitudes
    default_auto_field = 'django.db.models.BigAutoField' #Configuración del campo automático para claves primarias
    name = 'solicitudes' #Definimos el nombre de la aplicación a utilizar
