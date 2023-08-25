
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'), #Va al archivo de views y busca index.Siempre llevan comas entre lineas
    path('inicio', views.Inicio.as_view(),name='inicio'), #Página de inicio, muestra los botones esenciales si es que el usuario no se ha autenticado
    path('solicitud', views.Solicitud.as_view(), name='solicitud'), #Formulario de solicitudes, relacionarlo a solicitud de views.py
    path('solicitud_existente', views.solicitud_existente, name='solicitud_existente'), #URL para buscar solicitudes existentes. Si el usuario es funcionario, se habilita ULR para respuesta
    path('respuesta/<int:solicitud_id>/', views.respuesta_view, name='respuesta'), #ULR para responder las solicitudes. Se ingresa por medio de la lista de solicitudes
    path('reportes/graficas', views.graficas, name='graficas'), #Gráficas de respuesta, para fines de KPI
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'), #Creación de usuario, exclusivo de lso usuarios administradores (superuser)
    path('reportes/lista_solicitudes', views.lista_solicitudes, name='lista_solicitudes'), #Lista de solicitudes abiertas. Si el usuario está autenticado, le muestra un enlace para responder
    path('login/', views.custom_login, name='login'), #Pantalla de login tanto para servidores, como para administradores
    path('reset-password/', auth_views.PasswordResetDoneView.as_view(), name='password_reset'), #Reasignación de contraseña, en caso de olvidarla
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), #Reasignación de contraseña exitoso
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), #Confirmación de reasignación de contraseña
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), #Proceso de reasignación de contraseña exitoso
    path('logout/', views.custom_logout,name='logout'), #Cierre de sesión de usuarios autenticados, tanto para servidores públicos, como administradores
]