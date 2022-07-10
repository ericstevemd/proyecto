from rest_framework import serializers
from producto.models import ciudad


class ciudadSerializer(serializers.ModelSerializer):
    class Meta:
        model=ciudad
        fields='__all__'
