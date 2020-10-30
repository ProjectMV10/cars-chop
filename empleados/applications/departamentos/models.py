from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField('Nombre', max_length=100, blank=True, null=True, unique=True)
    activo = models.BooleanField('Activo', default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Departamento, self).save()

class Categorias(models.Model):
    categoria = models.CharField('Nombre Categoria', max_length=100)
    activo = models.BooleanField('Activo', default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)
    foto = models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.categoria

    def save(self):
        self.categoria = self.categoria.upper()
        super(Categorias, self).save()
    


    



