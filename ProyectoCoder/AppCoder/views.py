from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor
from AppCoder.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")



def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")


def cursos(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data
                  print(informacion)
                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 

                  curso.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= CursoFormulario() #F

      return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})




def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= ProfesorFormulario() 

      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})

def estudiantes(request):

      if request.method == 'POST':

            miFormulario = EstudianteFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email']) 

                  estudiante.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= EstudianteFormulario() 

      return render(request, "AppCoder/estudiantes.html", {"miFormulario":miFormulario})


def buscar(request):

      if  request.GET["camada"]: 

            camada = request.GET['camada'] 
            print(camada)
            cursos = Curso.objects.filter(camada__icontains=camada)
            print(cursos)
            return render(request, "AppCoder/cursos.html", {"cursos":cursos, "camada":camada})

      else:
            respuesta = "No enviaste datos"
            return render(request,"AppCoder/inicio.html", {"respuesta":respuesta})

def buscarProfe(request):

      if  request.GET["apellido"]: 

            apellido = request.GET['apellido'] 
            print(apellido)
            profesores = Profesor.objects.filter(apellido__icontains=apellido)
            print(profesores)
            return render(request, "AppCoder/profesores.html", {"profesores":profesores, "apellido":apellido})

      else:
            respuesta = "No enviaste datos"
            return render(request,"AppCoder/inicio.html", {"respuesta":respuesta})

def buscarEstudiante(request):

      if  request.GET["apellido"]: 

            apellido = request.GET['apellido'] 
            print(apellido)
            estudiantes = Estudiante.objects.filter(apellido__icontains=apellido)
            print(estudiantes)
            return render(request, "AppCoder/estudiantes.html", {"estudiantes":estudiantes, "apellido":apellido})

      else:
            respuesta = "No enviaste datos"
            return render(request,"AppCoder/inicio.html", {"respuesta":respuesta})

def leerProfesores(request):
      profesores=Profesor.objects.all()
      contexto={"profesores":profesores}
      return render(request,"AppCoder/leerProfesores.html", contexto)

def eliminarProfesor(request, profesor_nombre):
      profesor=Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()

      profesores=Profesor.objects.all()
      
      contexto={"profesores":profesores}
      return render(request, "AppCoder/leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
      profesor=Profesor.objects.get(nombre=profesor_nombre)

      if request.method=="POST":
            miFormulario = ProfesorFormulario(request.POST) #

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  profesor.nombre=informacion['nombre']
                  profesor.apellido=informacion['apellido']
                  profesor.email=informacion['email']
                  profesor.profesion=informacion['profesion']

                  profesor.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario=ProfesorFormulario(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
            return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario,"profesor_nombre":profesor_nombre})

class CursoList(ListView):
      model=Curso
      template_name="AppCoder/cursos_list.html"

class CursoDetalle(DetailView):
      model=Curso
      template_name="AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):
      model=Curso
      success_url="/AppCoder/curso/list"
      fields=['nombre','camada']

class CursoUpdate(UpdateView):
      model=Curso
      success_url="/AppCoder/curso/list"
      fields=['nombre','camada']

class CursoDelete(DeleteView):
      model=Curso
      success_url="/AppCoder/curso/list"
      