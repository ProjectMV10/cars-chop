from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class DeptoResource(resources.ModelResource):
    class Meta:
        model = Departamento

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categorias

class DeptoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'activo', 'fc', 'fm')
    resource_class = DeptoResource

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['categoria']
    list_filter = ('categoria',)
    list_display = ('id','categoria', 'activo', 'fc', 'fm', 'foto')
    resource_class = CategoriaResource


admin.site.register(Departamento, DeptoAdmin)
admin.site.register(Categorias, CategoriaAdmin)

# Register your models here.
