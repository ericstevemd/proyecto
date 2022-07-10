from rest_framework import serializers
from producto.models import proveedor


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model=proveedor
        fields='__all__'
