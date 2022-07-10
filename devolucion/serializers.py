from rest_framework import serializers
from producto.models import devolucion


class devolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model=devolucion
        fields='__all__'
