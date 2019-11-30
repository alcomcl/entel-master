from rest_framework.serializers import ModelSerializer
from apps.vendedor.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'email', 'fecha_nacimiento', 'admin')
