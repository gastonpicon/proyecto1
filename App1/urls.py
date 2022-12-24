"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from App1.views import *

urlpatterns = [
    path('curso/', curso),
    path('', inicio, name="inicio"),
    
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('busquedaComision/', busquedaComision, name="busquedaComision"),
    path('buscar/', buscar, name="buscar"),
    path('leerProfesores/', leerProfesores, name="leerProfesores"),
    path('eliminarProfesor/<id>', eliminarProfesor, name="eliminarProfesor"),
    path('editarProfesor/<id>', editarProfesor, name="editarProfesor"),
    #cbv
    path('estudiante/list/', EstudianteList.as_view(), name="estudiante_listar"),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name="estudiante_detalle"),
    path('estudiante/nuevo/', EstudianteCrear.as_view(), name="estudiante_crear"),
    path('estudiante/nuevo/', EstudianteCrear.as_view(), name="estudiante_crear"),
    path('estudiante/editar/<pk>', EstudianteUpdate.as_view(), name="estudiante_editar"),
    path('estudiante/borrar/<pk>', EstudianteDelete.as_view(), name="estudiante_editar"),

    path('login/', login_request, name='login'),
    path('register/', register, name='register'),


]
