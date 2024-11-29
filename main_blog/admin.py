from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'apellido', 'correo', 'fecha_registro', 'estado')
    list_filter = ('estado',)
    list_per_page = 25
    search_fields = ['nombre', 'apellido']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'estado', 'fecha_registro', 'fecha_modificacion')
    list_filter = ('estado',)
    list_per_page = 25
    search_fields = ['nombre']


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    
    list_display = ('titulo', 'estado', 'autor', 'categoria','fecha_publicacion')
    list_filter = ('autor', 'categoria', 'estado')
    list_per_page = 20
    search_fields = ['titulo']


@admin.register(ComentarioAutor)
class ComentarioAutorAdmin(admin.ModelAdmin):
    
    list_display = ('contenido', 'autor', 'publicacion', 'fecha_publicacion')
    list_filter = ('autor', 'publicacion')
    list_per_page = 30


@admin.register(ComentarioLector)
class ComentarioLectorAdmin(admin.ModelAdmin):
    
    list_display = ('contenido', 'lector', 'publicacion', 'fecha_publicacion')
    list_filter = ('lector', 'publicacion')
    list_per_page = 30
