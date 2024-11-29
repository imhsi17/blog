from django.db import models

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

