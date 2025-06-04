from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    paginas = models.IntegerField()
    anio = models.IntegerField()

    def __str__(self):
        return self.titulo
