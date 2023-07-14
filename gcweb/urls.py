from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('index/',index,name="index"),
    path('', index, name="index"),
    path('infoArte1/',infoArte1,name="infoArte1"),
    path('infoArte2/',infoArte2,name="infoArte2"),
    path('infoArte3/',infoArte3,name="infoArte3"),
    path('infoArte4/',infoArte4,name="infoArte4"),
    path('artistas/',artistas,name="artistas"),
    path('contacto/',contacto,name="contacto"),
    path('publicacionobra/', obras, name="publicacion"),
    path('registro/', registros_artista, name="registro"),
    path('obraspublicadas/',obrasPublicadas,name="obrasPublicadas"),
    path('obraspublicadasadmin/',obrasPublicadasAdmin,name="obrasPublicadasAdmin"),
    path('login_usuario',login_usuario,name="login_usuario"),
    path('indexAdmin/', inicioAdm, name= "inicioadmin"),
    path('indexArt/', inicioArt, name= "inicioart"),
    path('revisionobras/', revisionObras, name='revisionadmin'),
    path('aprobacionObras/<int:id>/', views.aprobacionObras, name='aprobacionObras'),
    path('rechazarObras/<int:publicacion_id>/', views.rechazarObras, name='rechazarObras'),
    path('agregar/',registros_artista,name='agregar'),
    path('listar',listar, name='listar'),
    path('modificar/<rut_artista>',modificar_artista,name='modificar'),
    path('eliminar_artista/<rut_artista>/', eliminar_artista, name="eliminar_artista"),
    path('estado_publicacion', estado_publicacion, name="estado_publicacion"),
    path('detalleArtista/<pk>',detalleArtista,name="detalleArtista"),
    path('galeria/', galeria, name="galeria"),
    path('postulacion/', postulacion, name="postulacion"),
    path('postulaciones/', postulaciones, name="postulaciones")
 

]