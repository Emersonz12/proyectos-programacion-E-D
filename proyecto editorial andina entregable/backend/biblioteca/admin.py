from django.contrib import admin
from biblioteca.models.autor import Autor
from biblioteca.models.libro import Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nacionalidad', 'edad')
    search_fields = ('nombre', 'nacionalidad')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'genero', 'paginas', 'anio')
    search_fields = ('titulo', 'genero')
