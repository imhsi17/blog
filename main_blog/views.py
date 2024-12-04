from django.shortcuts import render
from .models import Publicacion

# Create your views here.
def index(request):
    
    publicaciones = Publicacion.objects.filter(estado=True).order_by('-fecha_publicacion')
    
    return render(request, 'index.html', {'publicaciones':publicaciones})