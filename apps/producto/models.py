from django.db import models
from django.db.models import Avg, Count
from django.utils import timezone

class tipoProducto(models.Model) :
    nombre = models.CharField(max_length=40, null = False, blank = False)

    def __str__(self):
        return '{}'.format(self.nombre)


class Producto(models.Model) :
    nombre          = models.TextField(null = False, blank = False)
    precio          = models.IntegerField(null = False, blank = False)
    tipoProducto    = models.ForeignKey(tipoProducto, on_delete=models.CASCADE)
    #imagen          = models.FileField(null = False, blank = False)

    def __str__(self):
        return 'COD: ' + '{} |  {} | {}'.format(self.id, self.nombre, self.tipoProducto.nombre)


