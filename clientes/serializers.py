from rest_framework import serializers
from producto.models import cliente


class clientefacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model=cliente
        fields='__all__'
