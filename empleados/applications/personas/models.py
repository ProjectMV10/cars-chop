from django.db import models
from ckeditor.fields import RichTextField
from applications.departamentos.models import Departamento
from django.utils.text import slugify
from .managers import AutorManager, LibroManager, CategoriaManager

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=100)

    def __str__(self):
        return self.habilidad

    def save(self):
        self.habilidad = self.habilidad.upper()
        super(Habilidades, self).save()
    

class Empleado(models.Model):
    nombres = models.CharField('Nombre', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    telefono = models.CharField('Telefono', max_length=20, blank=True, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    activo = models.BooleanField('Activo', default=True)
    habilidades =models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    
    def __str__(self):
        return self.nombres + ' ' + self.apellidos

    class Meta:
        verbose_name = 'Mis Empleados'
        verbose_name_plural = 'Empleados de la Empresa'
        ordering = ['nombres'] #Order a de la A-Z con la - ordena de la Z-A

    
    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Empleado, self).save()


class Correo(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    message = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.email



class Post(models.Model):
    """Post model."""

    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    url = models.SlugField(max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Autor(models.Model):
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=100)
    nacinalidad = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    objects = AutorManager()

    def __str__(self):
        return self.nombre


class CategoriaLibro(models.Model):
    nombre = models.CharField(max_length=50)
    objects = CategoriaManager()

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    categoria = models.ForeignKey(CategoriaLibro, related_name="categoria_libro", on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField( max_length=100)
    fecha = models.DateField()
    portada = models.ImageField( upload_to="portadas", blank=True, null=True)
    visitas = models.PositiveIntegerField(blank=True, null=True)
    stok = models.PositiveIntegerField(default=0)
    objects = LibroManager()
    

    def __str__(self):
        return self.titulo


class Lector(models.Model):
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=100)
    nacinalidad = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    def save(self, *args, **kwargs):

        self.libro.stok = self.libro.stok - 1
        self.libro.save()

        super(Prestamo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.lector) + ' - ' + str(self.libro)





