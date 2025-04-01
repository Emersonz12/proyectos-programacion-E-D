from django.urls import path
from .views import manga_view

urlpatterns = [
    path('', manga_view, name='manga_view'),
]
