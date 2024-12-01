from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField

# Create your models here.
class Lector(models.Model):
    
    id = models.AutoField('Id', primary_key=True)
    correo = models.EmailField('Correo', unique=True, null=False, blank=False)
    nombre = models.CharField('Nombre', null=False, blank=False, max_length=150)
    apellido = models.CharField('Apellido', null=False, max_length=150)
    fecha_registro = models.DateField('Fecha Registro', auto_now=False, auto_now_add=True)
    estado = models.BooleanField('Estado Activo/Inactivo', default=True)
    
    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'
    
    def __str__(self) -> str:
        return f'{self.nombre.capitalize()} {self.apellido.capitalize()}'
    

class Categoria(models.Model):
    
    id = models.AutoField('Id', primary_key=True)
    nombre = models.CharField('Nombre', max_length=75)
    fecha_registro = models.DateField('Fecha Registro', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha Modificación', auto_now=True)
    estado = models.BooleanField('Categoria Activa/No Activa', default=True)
    
    def __str__(self) -> str:
        return self.nombre


class Publicacion(models.Model):
    
    id = models.AutoField('Id', primary_key=True)
    titulo = models.CharField('Título', blank=False, null=False, max_length=200)
    contenido = QuillField()
    descripcion = models.CharField('Descripción', max_length=150,
                                   default='Descripción de la publicación',
                                   null=False, blank=True)
    fecha_publicacion = models.DateField('Fecha Publicación', auto_now_add=True, auto_now=False)
    imagen = models.ImageField('Imagen', blank=True, upload_to='publicaciones')
    estado = models.BooleanField('Publicación Activa/No Activa', default=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    
    
    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
    
    def __str__(self) -> str:
        return self.titulo


class ComentarioAutor(models.Model):
    
    id = models.AutoField('Id', primary_key=True)
    contenido = models.TextField('Contenido', null=False, blank=False)
    fecha_publicacion = models.DateField('Fecha Publicación', auto_now_add=True, auto_now=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = 'Comentario Autor'
        verbose_name_plural = 'Comentarios Autor'


class ComentarioLector(models.Model):
    
    id = models.AutoField('Id', primary_key=True)
    contenido = models.TextField('Contenido', null=False, blank=False)
    fecha_publicacion = models.DateField('Fecha Publicación', auto_now_add=True, auto_now=False)
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = 'Comentario Lector'
        verbose_name_plural = 'Comentarios Lector'
    
