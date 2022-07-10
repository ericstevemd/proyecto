from rest_framework import serializers
from producto.models import tipo_articulo


class tipoarticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model=tipo_articulo
        fields='__all__'

