from django.db import models
from apps.producto.models import Producto
from apps.vendedor.models import User

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto, through='Detalle_Venta')
    total_venta = models.IntegerField(default=0, null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.vendedor)

    def __str__(self):
        return '{}'.format(self.producto)

    

class Detalle_Venta(models.Model) :
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cant_producto = models.IntegerField(default=1, null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.id_venta)


    def __str__(self):
        return '{}'.format(self.id_producto)
    
