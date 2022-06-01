from django.shortcuts import render, redirect

from Aplicaciones import Formulario
from .models import Datos
from .forms import DatosForm
# Create your views here.

def home(request):
    return render(request, "paginas/menu.html")

def datos(request):
    datos = Datos.objects.all()
    return render(request, "index.html", {'datos': datos}) 

def crear(request):
    formulario = DatosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('datos')
    return render(request, "registroDatos.html", {'formulario': formulario})

def editar(request, ID):
    Datoss = Datos.objects.get(ID=ID)
    formulario = DatosForm(request.POST or None, request.FILES or None, instance=Datos)
    return render(request, "editar.html", {'formulario': formulario})

def eliminar(request, ID):
    Datoss = Datos.objects.get(ID=ID)
    Datoss.delete()
    return redirect('datos')
    