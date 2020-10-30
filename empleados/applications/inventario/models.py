from django.db import models
from applications.departamentos.models import *
from django.contrib.auth.models import User 
from django.utils.text import slugify
from django.contrib.auth import get_user_model


class Producto(models.Model):
    codigo = models.CharField("Codigo Producto", max_length=100, blank=False, null=False, unique=True)
    nombre = models.CharField('Nombre Producto', max_length=150, blank=False, null=False, unique=True)
    precio = models.DecimalField('Precio Producto', max_digits=10, decimal_places=2, blank=False, null=False)
    activo = models.BooleanField('Activo', default=True)
    impuesto = models.BooleanField('ISV 15', default=False)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(blank=False, null=False)
    acercade = models.TextField('Acerca del Producto', blank=True, null=True)
    url = models.SlugField(max_length=255, blank=True, null=True, unique=True)
    existencia = models.IntegerField('Existencia Producto', blank=True, null=True)

    def __str__(self):
        return self.nombre
    


    class Meta:
        verbose_name = 'Productos Agregados'
        verbose_name_plural = 'Mis Productos'
        ordering = ['nombre'] #Order a de la A-Z con la - ordena de la Z-A

    
    def save(self):
        self.codigo = self.codigo.upper()
        self.nombre = self.nombre.upper()
        super(Producto, self).save()

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        self.url = slugify(self.nombre)
        super(Producto, self).save(*args, **kwargs)

class ImagenesProducto(models.Model):
    imagen = models.ImageField(blank=False, null=False)
    producto = models.ForeignKey('Producto', related_name="Producto_Imagen", on_delete=models.CASCADE)
    fc = models.DateTimeField(auto_now_add=True)


class CarritoCompra(models.Model):
    producto = models.ForeignKey(Producto, related_name="producto_carrito", on_delete=models.CASCADE)
    usuario = models.ForeignKey(get_user_model(), related_name="usuario_carrito", on_delete=models.CASCADE, blank=True, null=True)
    comprado = models.BooleanField('Comprado', default=False)
    cantidad = models.IntegerField('Cantidad', blank=False, null=False)
    precio = models.DecimalField('Precio', max_digits=10, decimal_places=2, blank=False, null=False)
    subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, blank=True, null=True)
    isv = models.DecimalField('Impuesto', max_digits=10, decimal_places=2, blank=True, null=True) 

    def save(self, *args, **kwargs):
        self.subtotal = float(self.cantidad * self.precio)
        if (self.producto.impuesto == True):
            self.isv = float(self.subtotal * float(15/100))
        else:
            self.isv = 0 
        #self.producto.existencia = self.producto.existencia - self.cantidad
        #self.producto.save()
    
        super(CarritoCompra, self).save(*args, **kwargs)

class CarUpdate(models.Model):
    cantidad_car = models.PositiveIntegerField()
    
    












    

# Create your models here.
