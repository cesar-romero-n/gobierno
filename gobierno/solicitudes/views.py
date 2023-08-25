from django.http import HttpResponse
from django.views import View

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required #exclusivo para login
from django.utils.decorators import method_decorator #Asegura que los usuarios estén autenticados
from django.db import connection

from .models import Solicitudes, Respuestas #importamos los modelos de Solicitudes y Respuestas, para interacción de ambas tablas
from .forms import SolicitudForm, RespuestaForm

#Importaciones para login de servidores públicos
from django.contrib.auth import authenticate, login #importaciones para autenticación
from django.http import HttpResponseForbidden #En caso que el usuario no esté autenticado, le muestra un mensaje
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect

def index(): 
    
    return HttpResponse("App de solicitudes") 

#Vista Inicio, para mostrar los elementos esenciales de interacción con la plataforma
class Inicio(View):
    template_name = 'inicio.html'
    
    def post(self, request): 
    
        return render(request, self.template_name) #Enviamos los elementos del template, para su almacenamiento
    
    def get(self, request):
        solicitudes = Solicitudes.objects.all() #Solicitamos todos los elementos del modelo Solicitudes
        
        return render(request, self.template_name, {'solicitudes': solicitudes})

#Vista Solicitud, para el envío de información de los ciudadanos
class Solicitud(View):
    template_name = 'solicitud.html'
    
    def post(self, request):
        form = SolicitudForm(request.POST) #Forma de Solicitud, con los datos de la solicitud del ciudadano
        if form.is_valid(): #Si la forma contiene todos los datos requeridos, guarda el registro en la base de datos
            solicitud = form.save()  # Guarda el objeto Solicitud y obtiene su referencia
            return render(request, self.template_name, {'form': form, 'solicitud': solicitud})
        return render(request, self.template_name, {'form': form})

    def get(self, request): #Regresa los datos de la solicitud, para fines de consulta y respuesta del servidor público
        form = SolicitudForm()
        return render(request, self.template_name, {'form': form})
    

#Logout de servidores públicos y administradores, regresándolos a la pantalla que ve el ciudadano 
def custom_logout(request):
    logout(request)
    return redirect('/solicitudes/inicio')

#Login de servidores públicos y administradores
def custom_login(request):
    template_name = 'login.html'

    if request.method == 'POST': #Si el usuario está intentando enviar su user y password, procede al siguiente proceso
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password) #Compara el user y password de la base de datos
        if  user is not None: #Si el resultado no devuelve un registro inexistente, permite el login
            login(request, user)
            if user.is_superuser: #Si el usuario es Administrador o superuser, lo redirige a crear usuario, de lo contrario a inicio
                return redirect('/solicitudes/crear_usuario')
            else:
                return redirect('/solicitudes/inicio')
        else:
            print('--------------------> No entró al Login') #Pruebas en terminal, no visibles en algún html
            messages.error(request, 'Credenciales inválidas') #Arroja Credenciales inválidas, en caso de no coincidir user y password
        
    return render(request, template_name)

#Vista para buscar una solcitud existente, y mostrar su respuesta del servidor público
class SolicitudExistente(View):
    template_name = 'solicitud_existente.html'
    
    def post(self, request): #Self nos hace la instancia al objeto, y request es la petición
    
        return render(request, self.template_name)
    
    def get(self, request): #Retorna la información de la solicitud existente
        solicitud_existente = Solicitudes.objects.all()
        
        return render(request, self.template_name, {'solicitud_existente': solicitud_existente})

#Vista para envío y revisión de respuestas de servidores públicos
def respuesta_view(request, solicitud_id):
    solicitud = get_object_or_404(Solicitudes, pk=solicitud_id) #Solicitud ligada a la llave primaria de la tabla Solicitudes
    
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid(): #Si el formulario es válido, guarda la respuesta
            respuesta = form.save(commit=False)
            respuesta.solicitud = solicitud
            respuesta.save()
            return redirect('lista_solicitudes')  # Redirige a la lista de solicitudes
    else:
        form = RespuestaForm() #Si el método no es POST, regresa un formulario vacío
    
    return render(request, 'respuesta.html', {'solicitud': solicitud, 'form': form})

#Vista para mostrar la lista de solicitudes enviadas al portal
def lista_solicitudes(request):
    solicitudes = Solicitudes.objects.prefetch_related('respuestas_set').all() #Prefetch_related se usa para optimizar la consulta y mosytrar las respuestas

#Context contiene la lista de solicitudes enviadas
    context = {
        'solicitudes': solicitudes 
    }

    return render(request, 'reportes/lista_solicitudes.html', context) #Regresa las solcitudes enviadas al portal, a la página lista_solicitudes

#Retorna las solciitudes existentes, por el método GET, utilizando la llave primaria id
def solicitud_existente(request):
    id = request.GET.get('id', None)
    solicitud = None
    error_message = None
    
    if id:
        try:
            solicitud = Solicitudes.objects.get(pk=id) #Busca la llave primaria. Si no la encuentra, regresa un mensaje de error
        except Solicitudes.DoesNotExist:
            error_message = "No se encontraron resultados"
    
    return render(request, 'solicitud_existente.html', {'solicitud': solicitud, 'error_message': error_message})

#Implementación pendiente, para fines de KPI, donde muestre la diferencia de fecha de envío y de respuesta ,así como la cantidad de reportes sin respuesta
def graficas(request):
    # Obtener el total de reportes con y sin respuesta
    reportes_con_respuesta = Respuestas.objects.count()
    reportes_sin_respuesta = Solicitudes.objects.filter(respuestas__isnull=True).count()

    # Obtener la diferencia promedio de fechas usando una consulta raw
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT AVG(CAST(respuestas.fecha_respuesta - solicitudes.fecha_reporte AS INT))
            FROM solicitudes
            LEFT JOIN respuestas ON solicitudes.id = respuestas.solicitud_id
            WHERE respuestas.fecha_respuesta IS NOT NULL
        """)
        diferencia_promedio = cursor.fetchone()[0]

    # Datos para la gráfica de reportes
    reportes_data = [reportes_con_respuesta, reportes_sin_respuesta]
    reportes_labels = ['Reportes Respondidos', 'Reportes Sin Respuesta']

    # Datos para la gráfica de fechas
    fechas_data = [diferencia_promedio if diferencia_promedio else 0]
    fechas_labels = ['Diferencia Promedio']

    context = {
        'reportes_data': reportes_data,
        'reportes_labels': reportes_labels,
        'fechas_data': fechas_data,
        'fechas_labels': fechas_labels,
    }

    return render(request, 'graficas.html', context)

#Vista para los administradores (Superusers)
def crear_usuario(request):
    if not request.user.is_superuser: #Si el usuario no está autenticado como administrador, le muestra mensaje de error en pantalla
        return HttpResponseForbidden("No cuentas con acceso para entrar al enlace de crear usuario")
    if request.method == 'POST': #Si el usuario es administrador, envía el username, password y email auth_user de la base de datos
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Crea el nuevo usuario, con los campos de nombre de usuario, contraseña y correo electrónico, para fines de recuperación de cuenta.
        user = User.objects.create_user(username=username, password=password, email=email)
        messages.success(request, f'Usuario {username} creado correctamente.')
        return redirect('crear_usuario')  # Redirige a la misma página después de la creación

    return render(request, 'crear_usuario.html')