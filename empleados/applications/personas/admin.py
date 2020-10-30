from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class EmpleadoResource(resources.ModelResource):
    class Meta:
        model = Empleado

class EmpleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres']
    filter_horizontal = ('habilidades',)
    list_filter = ('departamento','habilidades')
    list_display = ('nombres', 'apellidos', 'telefono', 'departamento', 'activo', 'full_name')

    def full_name(self, obj):
        print(obj)
        return obj.nombres + ' ' + obj.apellidos
    resource_class = EmpleadoResource

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(CategoriaLibro)
admin.site.register(Prestamo)
admin.site.register(Lector)
# Register your models here.
