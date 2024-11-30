from django.shortcuts import render
from .models import Publicacion

# Create your views here.
def index(request):
    
    publicaciones = Publicacion.objects.all()
    
    
    return render(request, 'base.html', {'publicaciones':publicaciones})