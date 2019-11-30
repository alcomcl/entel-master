from django.contrib import admin
from apps.venta import models as modelo

# Register your models here.

admin.site.register(modelo.Venta)
admin.site.register(modelo.Detalle_Venta)