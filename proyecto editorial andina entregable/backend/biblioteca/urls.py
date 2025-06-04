from django.urls import path, include
from rest_framework import routers
from .views import AutorViewSet, LibroViewSet

router = routers.DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'libros', LibroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
