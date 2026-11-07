

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('crear/', views.crear_aprendiz, name='crear_aprendiz'),
    path( 'editar/<str:documento>/', views.editar_aprendiz, name='editar_aprendiz'),
    path( 'eliminar/<str:documento>/', views.eliminar, name='eliminar'),
    path('buscar/', views.buscar_aprendiz, name='buscar_aprendiz'),
    path('mapa/', views.buscar_pokemon, name='pokemon'),
    path( 'mapa_interactivo/',views.mapa_interactivo,name='mapa_interactivo')
]