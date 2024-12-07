from django.urls import path
from .views import index, categoria, publicacion

urlpatterns = [
    path('', index, name='index'),
    path('categoria/<str:nombre>', categoria, name='categoria'),
    path('publicacion/<int:id_publicacion>', publicacion, name='publicacion')
]