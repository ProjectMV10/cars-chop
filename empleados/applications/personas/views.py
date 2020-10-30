from django.shortcuts import render, redirect
from django.template.loader import render_to_string, get_template 
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.views.generic import TemplateView, ListView, CreateView, DetailView, FormView
from .models import *
from .forms import *
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from applications.departamentos.models import Categorias
from applications.inventario.models import Producto, CarritoCompra
from django.db.models import Sum
from django.db.models import Count
from django.urls import reverse_lazy

# Vista basada en clases 
class MenuView(TemplateView):
    template_name = "base/base.html"

def PaginaPrincipal(request):
    producto = Producto.objects.order_by('-id')[:10] #limite de filtro
    categoria = Categorias.objects.order_by('-pk')
    carrito = CarritoCompra.objects.filter(comprado = False, usuario= request.user).order_by('-id')
    if request.user.is_authenticated:
        ct = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Sum('cantidad'))['total']
        subtotal = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Sum('subtotal'))['total']
        isv = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Sum('isv'))['total']
        if subtotal == None:
            total = 0
        else:
            total = (subtotal + isv)
    else:
        ct = 0
        total = 0
        isv = 0   
    diccionario = {
        'producto': producto,
        'ct': ct,
        'carrito': carrito,
        'total': total,
        'categoria': categoria,
    }
    return render(request, 'home/index.html', diccionario)

#Vista basada en funciones 
""" def index(request):
    try:
        pass
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'prueba.html') """


class HomeListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0, 20, 30, 40'] # EL queryset siempre va hacer referencia al nombre de una lista 

class ListEmpleados(ListView):
    queryset = Empleado.objects.all()
    context_object_name = 'listado'
    paginate_by = 10
    template_name = "personas/list_all.html"

class List_By_Area(ListView):
    template_name = 'personas/list_by_area.html'
    queryset = Empleado.objects.filter(
      departamento__nombre = 'CONTABILIDAD'  
    )
    #print(queryset)

class BuscarEmpleado(ListView):
    template_name = 'personas/list_busqueda.html'
    context_object_name = 'listado'

    def get_queryset(self):
        resultado = self.request.GET.get("resul", '')
        lista = Empleado.objects.filter(
            departamento__nombre = resultado
            )
        return lista

class EmpleaodCreateView(CreateView):
    model = Empleado
    template_name = "personas/add_empleado.html"
    fields = ('__all__')
    success_url = '.'

def Contacto(request):
    Contact_form = ContactForm
    diccionario = {
        'form':Contact_form,
    }
    if request.method == 'POST':
        form = Contact_form(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            telefono = request.POST.get('telefono')

            template = get_template('personas/email_content.txt')
            content = { 
                'name': request.POST.get('name'),
                'email': request.POST.get('email'),
                'message': request.POST.get('message'),
                'telefono': request.POST.get('telefono')

            }
            content = template.render(content)

            datos = EmailMessage(
                "Nuevo Mensaje de Cotacto Recibido",
                content,
                "Papelería San Diego" + "",
                ['mvmoii29@gmail.com'],
                headers = {'Reply To': email}
            )
            form.save()
            datos.send()
            messages.success(request, 'Solicitud enviada satisfactoriamente')
            return redirect('.')

    return render(request, 'personas/contactanos.html', diccionario )



class DetalleProductoView(DetailView):
    template_name = 'productos/producto_detalle.html'
    model = Producto
    
    def get_context_data(self, **kwargs):
        context = super(DetalleProductoView, self).get_context_data(**kwargs)
        context["mensaje"] = 'Detalles del producto' 
        return context


def VerCategoriasProducto(request, id):
    categoria = Categorias.objects.filter(activo = True, pk = id).first()
    ctx = {'categoria': categoria}
    
    return render (request, 'categorias/categoria_productos.html', ctx)


def verDetalleProducto(request, url):
    categoria = {}
    try:
        producto = Producto.objects.filter(url=url).first()
        carrito = CarritoCompra.objects.filter(usuario= request.user, producto=producto)
        carritolista = CarritoCompra.objects.filter(comprado = False, usuario = request.user).order_by('-pk')
        ct = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Sum('cantidad'))['total']
        subtotal = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Sum('subtotal'))['total']
        isv = CarritoCompra.objects.filter(comprado = False, usuario = request.user).aggregate(total=Sum('isv'))['total']
        if subtotal == None:
            total = 0
        else:
            total = (subtotal + isv)
    except Producto.DoesNotExist:
        raise Http404
    if producto == None:
        print('no hay productos aqui')
    else:
        c = producto.categoria.id
        categoria = Producto.objects.filter(categoria = c).exclude(url = url).order_by('-pk')[:10]
    context = {
        'producto': producto,
        'categoria': categoria,
        'carrito': carrito,
        'carritolista': carritolista,
        'ct': ct,
        'subtotal': subtotal,
        'isv': isv,
        'total': total,
    }
    return render(request, 'productos/producto_detalle.html', context)


class PostDetailView(DetailView):
    
    template_name = 'personas/detail.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'url'
    slug_url_kwarg = 'url'

class PostCreate(CreateView):
    template_name = 'personas/add_post.html'
    model = Post
    fields = ('title',)
    success_url = reverse_lazy('add_post')


class ListarAutores(ListView):
    template_name = "biblioteca/lista_autores.html"
    context_object_name = "obj"

    def get_queryset(self):
        palabra_buscada = self.request.GET.get("resul", "")
        
        return Autor.objects.buscar_autor3(palabra_buscada)



class ListarLibro(ListView):
    template_name = "biblioteca/lista_libros.html"
    context_object_name = "obj"

    def get_queryset(self):
        palabra_buscada = self.request.GET.get("resul", "")
        #fechainicial
        f1 = self.request.GET.get("fecha1", "")
        #fechafinal
        f2 = self.request.GET.get("fecha2", "") 
        if f1 and f2:
            return Libro.objects.buscar_libros2(palabra_buscada, f1, f2)
        else:
            return Libro.objects.buscar_libros(palabra_buscada)



class LibroDetalle(DetailView):
    model = Libro
    template_name='biblioteca/libro_detalle.html'


#vista creada con save
class RegistrarPrestamo(FormView):
    template_name = "biblioteca/add_prestamo.html"
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        prestamo = Prestamo(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            devuelto=False
        )
        prestamo.save()

        #libro=form.cleaned_data['libro']
        #libro.stok = libro.stok - 1
        #libro.save() 

        return super(RegistrarPrestamo, self).form_valid(form)


#vista creada con get_or_create
class AddPrestamo(FormView):
    template_name = "biblioteca/add_prestamo.html"
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        obj, created = Prestamo.objects.get_or_create(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            devuelto=False,
            #defaults={
            #    'fecha_prestamo': date.today() #en mi caso como la fecha la agrego automaticamente este paso lo omito pero si fuese creada manuelamente de esta forma la incluimos
            #}
        )
        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            ctx={}
            estado = True
            ctx['estado'] = estado
            return HttpResponseRedirect('.')


class AddPrestamoMuliple(FormView):
    template_name = "biblioteca/add_multiple_prestamo.html"
    form_class = PrestamoMultipleForm
    success_url = '.'

    def form_valid(self, form):
        print(form.cleaned_data['lector'])
        print(form.cleaned_data['libros'])
        
        return super(AddPrestamoMuliple, self).form_valid(form)
 



        


    

    










    
   
