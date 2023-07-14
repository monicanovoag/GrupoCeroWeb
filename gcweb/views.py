from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def index(request):
  
        
    return render(request, "index.html")

def artistas(request):

    artistas = Datos_Artista.objects.all()
    data={
        'artistas': artistas
    }

    if request.method == "POST":

        Valor_buscado = request.POST.get("valor_buscado")
        if Valor_buscado != "":
            artistas=Datos_Artista.objects.filter(nombre_artista = Valor_buscado)
            data["artistas"] = artistas
        else:
            data["artistas"] = Datos_Artista.objects.all()

    return render(request, "artistas.html",data)

def infoArte1(request):
    return render(request, "infoArte1.html")

def infoArte2(request):
    return render(request,"infoArte2.html")

def infoArte3(request):
    return render(request,"infoArte3.html")

def infoArte4(request):
    return render(request,"infoArte4.html")

def contacto(request):
    
    data={
        "form" : ContactoForm
    }

    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Mensaje enviado con éxito, nos contactaremos a la brevedad.")
        else:
            messages.error(request, "Error")
            data["form"] = formulario

    return render(request,"contacto.html", data)

@login_required
def obras(request):

    data = {
        'form': PublicacionForm,
    }

    if request.method == "POST":
        form = PublicacionForm (data=request.POST, files=request.FILES)
        
        if form.is_valid():
            nombre_obra = form.cleaned_data.get('nombre_obra')
            descripcion_obra = form.cleaned_data.get('descripcion_obra')
            tecnica_obra = form.cleaned_data.get('tecnica_obra')
            valor_obra = form.cleaned_data.get('valor_obra')
            categoria = form.cleaned_data.get('categoria')
            imagen_obra = form.cleaned_data.get('imagen_obra')

            obra = PublicacionArt()
            obra.nombre_obra = nombre_obra
            obra.descripcion_obra = descripcion_obra
            obra.tecnica_obra = tecnica_obra
            obra.valor_obra = valor_obra
            obra.categoria = categoria
            obra.imagen_obra = imagen_obra

            obra.artista=request.user
            obra.save()
            messages.success(request, 'Publicación a la espera de revisión')
            return redirect('inicioart')
        
        else: 
            form = PublicacionForm()

        return render(request,'publicacionObra.html', data)


            

    return render(request, "publicacionObra.html", data)

def obrasPublicadasAdmin(request):

    publicaciones = PublicacionArt.objects.all()

    data = {
        "publicaciones": publicaciones
    }

    return render(request, "obrasPublicadasAdmin.html", data)

def obrasPublicadas(request):

    publicaciones = PublicacionArt.objects.all()
    
    data = {
        "publicaciones": publicaciones
    }

    return render(request,"obrasPublicadas.html",data)

def login_usuario(request):
    print("Bienvenido " + request.user.username)
    if request.user.groups.filter(name='artista'):    
        return redirect(to='obrasPublicadas')
    else:   
        return redirect(to='revisionadmin')

def registros_artista(request):
    data = {
        'form' : ArtistaForm
    }
    if request.POST: 
        form = ArtistaForm(request.POST, request.FILES)
        if form.is_valid():

            rut = form.cleaned_data.get('rut_artista')
            nombre = form.cleaned_data.get('nombre_artista')
            apellido = form.cleaned_data.get('apellido_artista')
            correo = form.cleaned_data.get('correo')
            password = form.cleaned_data.get('password')
            foto = form.cleaned_data.get('foto')

            if User.objects.filter(email=correo).exists():
                messages.error(request, "El correo ya se encuentra registrado.")

    
            else:
                usu = User()
                usu.set_password(password)
                usu.email = correo
                usu.username = nombre
                usu.first_name = nombre
                usu.last_name = apellido
                grupo = Group.objects.get(name='artista')

                usu.save()

                artista = Datos_Artista()
                artista.rut_artista = rut
                artista.nombre_artista = nombre
                artista.apellido_artista = apellido
                artista.correo = correo
                artista.password = password  
                artista.foto = foto
                #artista.usuario = usu
                

                artista.save()

                usu.groups.add(grupo)
                messages.success(request, "Usuario creado con éxito")
                return redirect(reverse("login"))
            
                

    return render(request, "registration/registro.html", data)

def inicioAdm(request):
    return render(request,"baseAdmin.html")

def inicioArt(request):
    return render(request,"baseArtista.html")

def revisionObras(request):

    publicaciones = PublicacionArt.objects.all()

    data = {
        "publicaciones": publicaciones
    }

    return render(request, "revisionObras.html", data)

def aprobacionObras(request, id):

    publicacion = get_object_or_404(PublicacionArt, id=id)
    publicacion.estado = 1
    publicacion.save()  
    messages.success(request, 'La publicación ha sido aprobada')

    return redirect('revisionadmin')

def rechazarObras(request, publicacion_id):
    if request.method == 'POST':
        motivo_rechazo = request.POST.get('motivo_rechazo')
        publicacion = PublicacionArt.objects.get(id=publicacion_id)
        publicacion.estado = 2  # 2 representa el estado de "rechazado"
        publicacion.mensaje_rechazo = motivo_rechazo
        publicacion.save()
        messages.success(request, 'La publicación ha sido rechazada exitosamente.')
        return redirect('revisionadmin')
    else:
        messages.error(request, 'Se produjo un error al rechazar la publicación.')
        return redirect('revisionadmin')

def agregarArtista(request):
    data = {
        'form' : ArtistaForm
    }
    if request.method == 'POST': 
        form = ArtistaForm(request.POST,request.FILES)
        if form.is_valid():
            arts=form.save(commit=False)
            arts.usuarioCreadorDeCuenta = request.user
            arts.save()

            messages.success(request, "Artista creado con éxito")
        else:
            messages.success(request, "Hubo un error")
            data["form"] = form  
                
    return render(request,"mantenedor/artistas/agregar.html", data)

def listar(request):

    artistas = Datos_Artista.objects.all()

    data={
        'artistas': artistas
    }

    return render(request,"mantenedor/artistas/listar.html",data)

def modificar_artista(request, rut_artista):

    datos_Artista = get_object_or_404(Datos_Artista, rut_artista=rut_artista)

    data = {
        "form": ArtistaForm(instance=datos_Artista)
    }

    if request.method == 'POST':
        formulario = ArtistaForm(data=request.POST, files=request.FILES, instance=datos_Artista)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar")
        else:
            data["mensaje"] = "Hubo un error"
            data["form"] =  formulario


    return render(request, "mantenedor/artistas/modificar.html", data)

def eliminar_artista(request, rut_artista):
    datos_Artista = get_object_or_404(Datos_Artista, rut_artista=rut_artista)

    datos_Artista.delete()
    messages.success(request, "El Artista rut: "+ rut_artista + " fue eliminado correctamente")
    return redirect(to="listar")

def estado_publicacion(request):

    publicaciones = PublicacionArt.objects.all()
    
    data = {
        "publicaciones": publicaciones
    }

    return render(request, "estadoObrasArt.html", data)

def detalleArtista(request, pk):
    artista = get_object_or_404(Datos_Artista, pk=pk)
    data = {
        "a": artista
    }

    return render(request,"detalleArtista.html",data)

def galeria(request):

    publicaciones = PublicacionArt.objects.all()
    
    data = {
        "publicaciones": publicaciones
    }
    return render(request,"galeria.html",data)


def postulacion(request):

    postulacion = PostulacionForm

    data = {
        "form": postulacion
    }

    if request.method =="POST":
        postulacion = PostulacionForm(request.POST,request.FILES)
        if postulacion.is_valid():
            postulacion.save()
            messages.success(request, "Postulación realizada con éxito.")
        else:
            messages.error(request, "Error")
            data["form"] = postulacion


    return render(request, "postulacion.html",data)



def postulaciones(request):

    postulaciones = Postulacion.objects.all()

    data = {
        "postulaciones" :postulaciones 
    }

    return render(request, "postulacionadm.html", data)