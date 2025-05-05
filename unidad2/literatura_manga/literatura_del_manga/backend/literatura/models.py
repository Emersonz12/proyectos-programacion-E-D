from django.db import models

class Manga(models.Model):
    genero = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    volumenes = models.IntegerField()
    tema_principal = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.autor} - {self.tema_principal}"
