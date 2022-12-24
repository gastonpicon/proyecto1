from django.shortcuts import render
from .models import Curso, Profesor, Estudiante
from django.http import HttpResponse
from App1.forms import CursoForm, ProfeForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def curso(request):
    curso=Curso(nombre="AWS", comision=31105)
    curso.save()
    texto= f"Curso creado: nombre: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)

#CONFIGURACION INCIAL
#def inicio(request):
#    return HttpResponse("Inicio")
#
#def cursos(request):
#    return HttpResponse("Cursos")
#
#def estudiantes(request):
#    return HttpResponse("Estudiantes")
#
#def profesores(request):
#    return HttpResponse("Profesores")
#
#def entregables(request):
#    return HttpResponse("Entregables")
#
def inicio(request):
    return render(request, "App1/inicio.html")

def cursos(request):
    return render(request, "App1/cursos.html")
 
def estudiantes(request):
    return render(request, "App1/estudiantes.html")

def profesores(request):
    return render(request, "App1/profesores.html")

def entregables(request):
    return render(request, "App1/entregables.html")

def curso(request):
    cursito=Curso(nombre="curso creado con vista de prueba",comision=0)
    print("creando curso")
    cursito.save()
    texto=f"cursito creado"
    return HttpResponse(texto)

"""def cursoFormulario(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        comision=request.POST["comision"]

        curso=Curso(nombre=nombre, comision=comision)
        curso.save()

        return render(request, "App1/inicio.html")
    
    return render(request, "App1/cursoFormulario.html")"""

def cursos(request):
    if request.method=="POST":
        form=CursoForm(request.POST)
        print("------------------")
        print(form)
        print("------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            comision=informacion["comision"]
            curso=Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        formulario=CursoForm()
        return render(request, "App1/cursos.html", {"formulario":formulario})

def profesores(request):
    if request.method=="POST":
        form=ProfeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            profesores=Profesor.objects.all()
            return render(request, "App1/leerProfesores.html", {"profesores":profesores})
    else:
        form=ProfeForm()
    return render(request, "App1/profesores.html", {"formulario":form})

def busquedaComision(request):
    return render(request, "App1/busquedaComision.html")

def buscar(request):
    if request.GET["comision"]:
    
        comision=request.GET["comision"]
#   respuesta=f"estoy buscando la comision {comision}"

# traeme de a base todos los cursos con tengan esa comision
        cursos=Curso.objects.filter(comision=comision)

        return render(request, "App1/resultadoBusqueda.html", {"cursos":cursos})
    else:
        return render(request, "App1/busquedaComision.html", {"mensaje":"CHE INGRESE UNA COMISION"})
    return HttpResponse(respuesta)
    
def leerProfesores(request):
    profesores=Profesor.objects.all()
    print(list(profesores))
    return render(request, "App1/leerProfesores.html",{"profesores":profesores})

def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    profesor.delete()
    profesores=Profesor.objects.all()
    return render(request, "App1/leerProfesores.html",{"profesores":profesores})

def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    if request.method=="POST":
        form=ProfeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profesor.nombre=info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.email=info["email"]
            profesor.save()
            profesores=Profesor.objects.all()
            return render(request, "App1/leerProfesores.html",{"profesores":profesores})
    else:
        form=ProfeForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email})
        return render(request, "App1/editarProfesores.html", {"formulario":form, "profesor":profesor})


class EstudianteList(ListView):
    model=Estudiante
    template_name="App1/leerEstudiantes.html"

class EstudianteDetalle(DetailView):
    model=Estudiante
    template_name="App1/estudiante_detalle.html"

class EstudianteCrear(CreateView):
    model=Estudiante
    success_url=reverse_lazy('estudiante_listar')
    fields=['nombre','apellido','email']

class EstudianteUpdate(UpdateView):
    model=Estudiante
    success_url=reverse_lazy('estudiante_listar')
    fields=['nombre','apellido','email']

class EstudianteDelete(DeleteView):
    model=Estudiante
    success_url=reverse_lazy('estudiante_listar')



def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'App1/login.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, "App1/login.html", {"formulario":form, "mensaje":"use o pass incorrecto"})
        else:
            return render(request, "App1/login.html", {"formulario":form, "mensaje":"use o pass incorrecto"})
    else:
        form=AuthenticationForm()
        return render(request, "App1/login.html", {"formulario":form})

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, "App1/incio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "App1/register.html", {"mensaje":"formulario invalido"})

    else:
        form=UserCreationForm()
        return render(request, "App1/register.html", {"formulario":form})