from django import forms
from .models import *

class ContactoForm(forms.ModelForm):

    class Meta: 
        model = Contacto
        fields = "__all__"  

class PublicacionForm (forms.ModelForm):
    class Meta: 
        model = PublicacionArt
        fields = ["nombre_obra", "descripcion_obra","tecnica_obra", "valor_obra", "categoria", "imagen_obra"]

class ArtistaForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Datos_Artista
        fields = ["rut_artista","nombre_artista","apellido_artista","correo","password","foto"]

class PostulacionForm(forms.ModelForm):
    class Meta:
        model = Postulacion
        fields = "__all__"
