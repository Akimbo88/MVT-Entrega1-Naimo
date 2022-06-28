from django.urls import path

from AppCoder import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('cursoFormulario', views.cursos, name="CursoFormulario"),
    path('profesorFormulario', views.profesores, name="ProfesorFormulario"),
    path('buscar/', views.buscar),
    path('buscarProfe/', views.buscarProfe),
    path('buscarEstudiante/', views.buscarEstudiante),
    path('leerProfesores', views.leerProfesores, name="LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>', views.eliminarProfesor,name="eliminarProfesor"),
    path('editarProfesor/<profesor_nombre>', views.editarProfesor,name="editarProfesor"),
    path('curso/list',views.CursoList.as_view(),name="List"),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name="Detail"),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name="New"),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name="Delete")
]

