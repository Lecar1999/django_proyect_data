from django.urls import path
from . import views
from .import admin

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('datos', views.datos, name='datos'),
    path('editar', views.editar, name='editar'),
    path('crear', views.crear, name='crear'), 
    path('eliminar/<int:ID>', views.eliminar, name='eliminar'),
    path('editar/<int:ID>', views.editar, name='editar'),

]