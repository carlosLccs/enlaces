from django import forms
from django.forms import ModelForm
from .models import Enlace

class EnlaceForm(forms.ModelForm):
    class Meta:
        model = Enlace
        fields = '__all__'
        labels = {
            'titulo':'Titulo',
            'descripcion':'Descripcion',
            'enlace':'Enlace'
        }
       

     