
from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

class ProductoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_filter = ('categoria',)
    list_display = ('codigo', 'nombre', 'precio', 'categoria', 'activo', 'impuesto')


class CarritoCompraResource(resources.ModelResource):
    class Meta:
        model = CarritoCompra

class CarritoCompraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'producto', 'usuario', 'cantidad', 'precio', 'subtotal', 'comprado')


admin.site.register(Producto, ProductoAdmin)
admin.site.register(ImagenesProducto)
admin.site.register(CarritoCompra, CarritoCompraAdmin)
admin.site.register(CarUpdate)