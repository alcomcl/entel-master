from rest_framework.serializers import ModelSerializer
from apps.producto.models import Producto


class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'precio', 'tipoProducto')