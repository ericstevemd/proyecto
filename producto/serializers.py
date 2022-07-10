from rest_framework import serializers
from producto.models import porducto


class porductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=porducto
        fields='__all__'
