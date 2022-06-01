from dataclasses import fields
from django import forms
from .models import Datos

class DatosForm(forms.ModelForm):
    class Meta:
        model = Datos
        fields = '__all__'
