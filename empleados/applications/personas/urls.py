from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


#def pruebaURL(a,b):
    #return a + b;
#print("la cantidad es:", pruebaURL(10,20));
urlpatterns = [
    path('', views.PaginaPrincipal, name="inicio"),
    path('lista/', views.HomeListView.as_view()),
    path('menu_principal/', views.MenuView.as_view(), name="menu_principal"),
    path('list_all/', views.ListEmpleados.as_view()),
    path('list_area/', views.List_By_Area.as_view()),
    path('list_busqueda/', views.BuscarEmpleado.as_view()),
    path('add_empleado/', views.EmpleaodCreateView.as_view()),
    path("listado_autores", views.ListarAutores.as_view(), name="listado_autores"),
    path("listado_libros", views.ListarLibro.as_view(), name="listado_libros"),
    path('contacto/', views.Contacto, name="contacto"),
    path("libro_detalle/<int:pk>", views.LibroDetalle.as_view(), name="libro_detalle"),
    path('add_post', views.PostCreate.as_view(), name="add_post"),
    path("add_prestamo/", views.AddPrestamo.as_view(), name="add_prestamo"),
    path("add_multiple_prestamo/", views.AddPrestamoMuliple.as_view(), name="add_multiple_prestamo"),
    #path('detalle_producto/<int:id>/', views.verDetalleProducto , name="detalle_producto"),
    #path('', views.index)
    #path('prueba/', pruebaURL, name='prueba')
    path(
    route='detalle_producto/<slug:url>/',
    view=views.verDetalleProducto,
    name='detalle_producto'
),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)