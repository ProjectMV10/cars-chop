from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('categoria_producto/tinta-epson', views.ListCategoriaTintaEpson.as_view(), name="tinta-epson"),
    path('agregar_carrito', views.agregarProductoCarrito, name="agregar_carrito"),
    path('micarrito', views.miCarrito, name="micarrito"),
    path('eliminar_producto/<int:id>', views.eliminarProductoCarrito, name="eliminar_producto"),
    path('nuevoProductoCarrito/', views.nuevoProductoCarrito.as_view(), name="nuevoProductoCarrito"),
    path('modificarcarrito/<int:pk>', views.ModificarCantidadCarrito.as_view(), name="modificarcarrito"),
    path("limpiarcarrito/", views.LimpiarCarrito.as_view(), name="limpiarcarrito"),
    path("actualizarcarrito/", views.AddCarView.as_view(), name="actualizarcarrito"),
    path("actualizarcanproductos/<int:pk>", views.ActulizarCanProd.as_view(), name="actualizarcanproductos"),
    path('modifacar_product_car/<int:id>/', view=views.ActulizarCarritoProd, name='modifacar_product_car'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)