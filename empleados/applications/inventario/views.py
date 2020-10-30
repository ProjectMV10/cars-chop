from django.shortcuts import render, redirect
from django.template.loader import render_to_string, get_template 
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, View, FormView
from .models import *
from applications.departamentos.models import Categorias
from applications.inventario.models import Producto, CarritoCompra
from django.urls import reverse_lazy
from django.db.models import Sum
from django.db.models import Count
from django.urls import reverse
from .forms import*
from django.contrib.auth.models import User 



class ListCategoriaTintaEpson(ListView):
    template_name = 'productos/categoria_tintaempson.html'
    context_object_name='obj'
    queryset = Producto.objects.filter(activo = True,
      categoria__categoria = 'TINTA EXPSON L575'  
    )

    def get_context_data(self, **kwargs):
        context = super(ListCategoriaTintaEpson, self).get_context_data(**kwargs)
        context["queryset"] = 'queryset'
        return context

class agregarCarrito(CreateView):
  model = CarritoCompra
  fields = ('producto', 'usuario', 'cantidad', 'precio')
  success_url = reverse_lazy('tinta-epson')
  

def agregarProductoCarrito(request):
    diccionario={}
    if request.method=='POST':
        _producto=request.POST['producto']
        _cantidad=request.POST['cantidad']
        _precio=request.POST['precio']
        frm=CarritoCompra(
            producto=Producto.objects.get(pk=_producto),
            cantidad=_cantidad,
            precio=_precio
                )
        print(_producto)
        frm.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, "horme/index.html", diccionario)


class nuevoProductoCarrito(View):

  def post(self, request, *args, **kwargs):
    p = request.POST['producto']
    u = request.POST['usuario']
    if request.user.is_authenticated:
      CarritoCompra.objects.create(
        producto = Producto.objects.get(pk=p),
        usuario = User.objects.get(pk=u),
        cantidad = int(request.POST['cantidad']),
        precio = float(request.POST['precio']),
    )
    else:
      pass
      #CarritoCompra.objects.create(
        #producto = Producto.objects.get(pk=p),
        #cantidad = int(request.POST['cantidad']),
        #precio = float(request.POST['precio']),
    #)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

#class nuevoProductoCarrito(CreateView):
  #model = CarritoCompra
  #fields = ('producto', 'usuario','cantidad', 'precio',)
  #success_url = reverse_lazy('inicio')
  #def get_success_url(self):
    #return "detalle_producto/{}/".format(self.object.producto.url)


class ModificarCantidadCarrito(UpdateView):
  model = CarritoCompra
  fields = ('cantidad',)
  success_url = reverse_lazy('micarrito')


class LimpiarCarrito(View):

  def post(self, request, *args, **kwargs):

    CarritoCompra.objects.all().delete()

    return HttpResponseRedirect(
      reverse('micarrito')
    )


def miCarrito(request):
  try:
    carrito = CarritoCompra.objects.filter(comprado = False, usuario = request.user).order_by('-pk')
    usuario = request.user
    print(usuario)
    ct = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Sum('cantidad'))['total']
    subtotal = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Sum('subtotal'))['total']
    isv = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Sum('isv'))['total']
    if subtotal == None:
      total = 0
    else:
      total = (subtotal + isv)
    contar = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Count('pk'))['total']
  except CarritoCompra.DoesNotExist:
    raise Http404
  cxt = {'carrito': carrito,
          'ct': ct,
          'subtotal': subtotal,
          'isv': isv,
          'total': total,
          'contar': contar,
  } 

  return render(request, 'micarrito/micarrito.html', cxt)

def eliminarProductoCarrito(request, id):
  template_name = 'micarrito/eliminar_prodcarrito.html'
  producto = CarritoCompra.objects.get(id = id)
  ctx = {
      'producto': producto
      }
  if request.method == "POST":
    prod = producto.producto.id #Octego el Id del prodcuto y lo almaceno en lo capturo en la variable prod
    exis = Producto.objects.get(id = prod) # octengo todos los valores de la Tabla producto una vez que le mando la variable de Id Capturado en Prod
    exis.existencia = exis.existencia + producto.cantidad #sumo la cantidad de productos que se van eliminar del carrito
    exis.save()# una vez que realizo todo el procedo anterior lo salvo con el metodo save que sirve para almacenar si el registro existe y para actualizar si ya existe
    producto.delete() #posteriormente elimino del carrito el producto
    return redirect('micarrito')

  return render(request, template_name, ctx)


def ActulizarCarritoProd(request, id):
  product = Producto.objects.get(pk=id)
  if request.method == "POST":
    cantidad = int(request.POST['cantidad'])
    carritoprod = CarritoCompra.objects.get(usuario = request.user, producto = product.id)
    carritoprod.cantidad = int(carritoprod.cantidad) + int(cantidad)
    carritoprod.save()
  return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

 

class ActulizarCanProd(View):

  def post(self, request, *args, **kwargs):

    can = CarritoCompra.objects.get(id=self.kwargs['pk'])
    print(can)
    if can.cantidad > 0:
      #can.cantidad = can.cantidad + 1
      can.save()


    return HttpResponseRedirect(
      reverse('micarrito')
    )



class AddCarView(FormView):
    template_name = 'micarrito/micarrito.html'
    form_class = CarForm
    success_url = reverse_lazy('micarrito')
    
    def form_valid(self, form):
      productos_en_car = CarritoCompra.objects.all() 
      print(productos_en_car)
      carritos = []
      for l in str(form.cleaned_data['cantidad']):
        print(form.cleaned_data['cantidad'])
        carrito = CarUpdate(
          cantidad_car=form.cleaned_data['cantidad']
        )
        carritos.append(carrito)
      CarUpdate.objects.bulk_create(
        carritos
      )  
      #CarritoCompra.objects.bulk_update(ventas_detalle, ['cantidad']) 
      return super(AddCarView, self).form_valid(form)








# Create your views here.
