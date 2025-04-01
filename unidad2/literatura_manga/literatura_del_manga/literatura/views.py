from django.shortcuts import render
from .forms import MangaForm

def manga_view(request):
    if request.method == 'POST':
        form = MangaForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el formulario en la base de datos
            form = MangaForm()  # Reiniciar el formulario después de guardar
    else:
        form = MangaForm()

    return render(request, 'literatura/manga.html', {'form': form})
