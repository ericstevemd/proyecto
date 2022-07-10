from rest_framework import serializers
from producto.models import detallefactura


class detallefacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model=detallefactura
        fields='__all__'
