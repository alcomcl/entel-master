from rest_framework.serializers import ModelSerializer
from apps.venta.models import Venta

class VentaSerializer(ModelSerializer):
    class Meta:
        model = Venta
        fields = ('id', 'vendedor', 'fecha', 'total_venta')