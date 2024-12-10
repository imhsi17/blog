from django.urls import path
from .views import (index, categoria, publicacion,
                    registro_lector, inicio_sesion_autor,
                    cerrar_sesion)

urlpatterns = [
    path('', index, name='index'),
    path('login/', inicio_sesion_autor, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('categoria/<str:nombre>', categoria, name='categoria'),
    path('publicacion/<int:id_publicacion>', publicacion, name='publicacion'),
    path('registro/', registro_lector, name='registro')
]