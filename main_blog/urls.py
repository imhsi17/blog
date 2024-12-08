from django.urls import path
from .views import index, categoria, publicacion, registro_lector

urlpatterns = [
    path('', index, name='index'),
    path('categoria/<str:nombre>', categoria, name='categoria'),
    path('publicacion/<int:id_publicacion>', publicacion, name='publicacion'),
    path('registro/', registro_lector, name='registro')
]