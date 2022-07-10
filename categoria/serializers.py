from rest_framework import serializers
from producto.models import categoria


class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=categoria
        fields='__all__'
