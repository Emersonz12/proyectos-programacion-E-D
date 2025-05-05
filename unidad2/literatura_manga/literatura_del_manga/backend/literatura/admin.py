from django.contrib import admin
from .models import Manga

@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('autor', 'genero', 'volumenes', 'tema_principal')
    search_fields = ('autor', 'genero', 'tema_principal')
