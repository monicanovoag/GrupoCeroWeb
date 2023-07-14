from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Datos_Artista(models.Model):
    rut_artista=models.CharField(max_length=10)
    nombre_artista=models.CharField(max_length=50)
    apellido_artista=models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    foto= models.ImageField(null=True, upload_to='artista')
    usuarioCreadorDeCuenta = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

  
    def __str__(self):
        return self.nombre_artista
    

tipos_contacto = [
    [0, "Consulta"],
    [1, "Sugerencia"],
    [2, "Solicitar Creacion De cuenta"]

]

class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=50)
    correo_contacto = models.CharField(max_length=100)
    telefono_contacto = models.IntegerField()
    mensaje_contacto = models.TextField()
    tipos_contacto = models.IntegerField(choices=tipos_contacto)
    def __srt__(self):
        return self.nombre_contacto + " "+self.correo_contacto


class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


estados = [
    [0, "En Espera"],
    [1, "Aprobado"],
    [2, "Rechazado"]
]

class PublicacionArt(models.Model):

    nombre_obra = models.CharField(max_length=50)
    descripcion_obra = models.TextField(max_length=200)
    tecnica_obra = models.CharField(max_length=50)
    valor_obra = models.PositiveSmallIntegerField()
    categoria=models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True)
    artista=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    imagen_obra = models.ImageField(upload_to="obras", null=True)
    estado = models.IntegerField(choices=estados, default=0)
    mensaje_rechazo = models.TextField(max_length=200, null=True)


    def __str__(self):
        return self.nombre_obra


estado_civil = [
    [0, "Seleccionar"],
    [1, "Soltero"],
    [2, "Casado"],
    [3, "Separado"],
    [4, "Divorciado"],
    [5, "Viudo"]
]

class Postulacion(models.Model):
    
    nombre_postulante = models.CharField(max_length=50)
    rut_postulante = models.CharField(max_length=10)
    edad_postulante = models.IntegerField()
    estado_civil_postulante = models.IntegerField(choices=estado_civil, default=0)
    imagen_postulante = models.ImageField(upload_to="postulantes", null=True)
    curriculum_postulante = models.FileField(upload_to= "curriculum_postulante", null=True)






