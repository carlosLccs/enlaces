from django.db import models

class Enlace(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    enlace = models.CharField(max_length=250)

    def __str__(self):
        return self.titulo
