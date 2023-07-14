from django.contrib import admin
from .models import *

# Register your models here.

class Datos_Artista_Admin(admin.ModelAdmin):
    list_display=['nombre_artista','apellido_artista','rut_artista']
    list_editable=['apellido_artista']
    search_fields=['rut_artista']

class CategoriaAdmin(admin.ModelAdmin):
    list_display=['nombre']

class ContactoAdmin(admin.ModelAdmin):
    list_display=['nombre_contacto','telefono_contacto','telefono_contacto','correo_contacto']
    list_editable=['correo_contacto']
    search_fields=['nombre_contacto']
    list_filter=['tipo_contacto']

class PublicacionAdmin (admin.ModelAdmin):
    list_display=['nombre_artista','descripcion_artista','nombre_obra','descripcion_obra','tecnica_obra','valor_obra']  
    list_editable = ['nombre_obra']
    search_fields = ['nombre_artista']



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Datos_Artista,Datos_Artista_Admin)
admin.site.register(Contacto)
admin.site.register(PublicacionArt)

