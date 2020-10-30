from django.shortcuts import render
from .models import *
from applications.inventario.models import Producto, CarritoCompra
from django.db.models import Sum
from django.db.models import Count


def VerCategoriasProducto(request, id):
    categorias = Categorias.objects.filter(activo = True, pk = id).first()
    categoria = Categorias.objects.filter(activo = True).order_by('-pk')
    productos = Producto.objects.filter(activo = True, categoria = id)
    ct = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Sum('cantidad'))['total']
    subtotal = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Sum('subtotal'))['total']
    isv = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Sum('isv'))['total']
    carrito = CarritoCompra.objects.filter(comprado = False, usuario = request.user).order_by('-id')
    if subtotal == None:
        total = 0
    else:
        total = (subtotal + isv)
    ctx = {'categorias': categorias,
           'productos': productos,
           'categoria': categoria,
           'ct': ct,
           'subtotal': subtotal,
           'carrito': carrito,
           'isv': isv,
           'total': total,
        }
    
    return render (request, 'categorias/categoria_productos.html', ctx)

# Create your views here.
