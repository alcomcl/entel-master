from django.contrib import admin
from apps.producto import models as modelo
# Register your models here.

admin.site.register(modelo.Producto)
admin.site.register(modelo.tipoProducto)
