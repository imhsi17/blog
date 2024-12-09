from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib import messages
from .models import Publicacion, Categoria, Lector, ComentarioAutor, ComentarioLector

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
    
    try:
        publicacion = Publicacion.objects.get(pk=id_publicacion, estado=True)
        categoria_publicacion = publicacion.categoria
        otras_publicaciones = Publicacion.objects.filter(
            categoria=categoria_publicacion,
            estado=True).exclude(
                pk=id_publicacion).order_by('-fecha_publicacion')[:3]
        categorias = Categoria.objects.filter(estado=True).order_by('-fecha_registro')
        autor_comentarios = ComentarioAutor.objects.filter(
            publicacion=publicacion).order_by('-fecha_publicacion')
        lector_comentarios = ComentarioLector.objects.filter(
            publicacion=publicacion).order_by('-fecha_publicacion')
        
        context = {
            'publicacion':publicacion,
            'categorias':categorias,
            'otros':otras_publicaciones,
            'autor_comentarios':autor_comentarios,
            'lector_comentarios':lector_comentarios
        }
        
        if request.method=='POST' and request.user.is_authenticated:
            comentario = request.POST['comentario']
            comentario_autor = ComentarioAutor(
                contenido = comentario,
                autor = request.user,
                publicacion = publicacion,
            )
            comentario_autor.save()
            
            return render(request, 'publicacion.html', context)
        
        if request.method=='POST':
            correo = request.POST['correo']
            comentario = request.POST['comentario']
            
            try:
                lector = Lector.objects.get(correo=correo)
                print('Todo correcto')
                comentario_lector = ComentarioLector(
                    contenido = comentario,
                    lector = lector,
                    publicacion = publicacion
                )
                comentario_lector.save()
                return render(request, 'publicacion.html', context)
            
            except Lector.DoesNotExist:
                
                messages.error(request, 'Correo inválido. Registrese para publicar comentarios.')
                print('Hubo un error')
                return redirect(f'/publicacion/{id_publicacion}')
        
        return render(request, 'publicacion.html', context)
    
    except Publicacion.DoesNotExist:
        
        return render(request, 'error.html')

def registro_lector(request):
    
    mensaje = ''
    if request.method=='POST':
        
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        
        try:
            lector = Lector.objects.get(correo=correo)
            if  lector:
                
                mensaje = 'El correo que ingresó ya fue registrado'
                return render(request, 'registro.html', {'mensaje':mensaje})

        except:
            
            try:
                validate_email(correo)
                nuevo_lector = Lector(
                    nombre = nombre,
                    apellido = apellido,
                    correo = correo
                )
                nuevo_lector.save()
                
                return redirect('/')
            
            except:
                        
                mensaje = 'Ingrese una dirección de correo válida.'
                return render(request, 'registro.html', {'mensaje':mensaje})
        
    return render(request, 'registro.html', {'mensaje':mensaje})