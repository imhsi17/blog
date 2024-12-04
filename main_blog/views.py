from django.shortcuts import render
from .models import Publicacion, Categoria

# Create your views here.
def index(request):
    
    publicaciones = Publicacion.objects.filter(estado=True).order_by('-fecha_publicacion')
    categorias = Categoria.objects.filter(estado=True).order_by('-fecha_registro')
    
    context = {
        'publicaciones':publicaciones,
        'categorias':categorias
    }
    
    return render(request, 'index.html', context)