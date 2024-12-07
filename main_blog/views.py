from django.shortcuts import render
from .models import Publicacion, Categoria

# Create your views here.
def index(request):
    
    publicaciones = Publicacion.objects.filter(estado=True,
                    categoria__estado=True).order_by('-fecha_publicacion')
    categorias = Categoria.objects.filter(estado=True).order_by('-fecha_registro')
    
    context = {
        'publicaciones':publicaciones,
        'categorias':categorias
    }
    
    return render(request, 'index.html', context)

def categoria(request, nombre):
    
    categoria = Categoria.objects.get(nombre=nombre)
    nombre_categoria = nombre
    publicaciones = Publicacion.objects.filter(estado=True,
                    categoria=categoria,
                    categoria__estado=True).order_by('-fecha_publicacion')
    categorias = Categoria.objects.filter(estado=True).order_by('-fecha_registro')
    
    context = {
        'publicaciones':publicaciones,
        'categorias':categorias,
        'categoria':nombre_categoria
    }
    
    return render(request, 'categoria.html', context)

def publicacion(request, id_publicacion):
    
    publicacion = Publicacion.objects.get(pk=id_publicacion, estado=True)
    categorias = Categoria.objects.filter(estado=True).order_by('-fecha_registro')
    
    context = {
        'publicacion':publicacion,
        'categorias':categorias
    }
    
    return render(request, 'publicacion.html', context)
    