from rest_framework import serializers
from producto.models import factura


class facturaSerializer(serializers.ModelSerializer):
    class Meta:
        model=factura
        fields='__all__'
