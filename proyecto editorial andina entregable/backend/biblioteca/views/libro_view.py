from rest_framework import viewsets
from biblioteca.models import Libro
from biblioteca.serializers import LibroSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
