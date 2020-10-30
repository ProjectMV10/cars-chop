import datetime

from django.db import models
from django.db.models import Q


class AutorManager(models.Manager):

    def buscar_autor(self, resul):

        resultado = self.filter(nombre__icontains=resul).exclude(edad = 80)
        # icostains no hara una busqueda haga coincidencia con las palabras ingresadas y que excluya los que tiene una edad de 80 años
        return resultado

    
    def buscar_autor2(self, resul):

        resultado = self.filter(
            Q(nombre__icontains=resul) | Q(apellido__icontains=resul))
            #Q nos va filtrar con el operador Or una busqueda que haga coicindencia por nombres o apellidos con las palabras ingresadas
        return resultado

    def buscar_autor3(self, resul):

        resultado = self.filter(
            edad__gt=70, #mayor que 
            edad__lt=100  #menor que 
        )
            # gt me filtra la edad que sea mayor que 79 y lt los que son menores de 90 
        return resultado


class LibroManager(models.Manager):

    def buscar_libros(self, resul):

        resultado = self.filter(titulo__icontains=resul)
        # icostains no hara una busqueda haga coincidencia con las palabras ingresadas
        return resultado

    def buscar_libros2(self, resul, fecha1, fecha2):

        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()  
        resultado = self.filter(titulo__icontains=resul, fecha__range=(date1, date2))
        # icostains no hara una busqueda haga coincidencia con las palabras ingresadas
        return resultado


class CategoriaManager(models.Manager):

    def categoria_autores(self, autor_id):

        return self.filter(
            categoria_libro__autores__id=autor_id
        ).distinct()
