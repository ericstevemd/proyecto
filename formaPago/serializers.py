from rest_framework import serializers
from producto.models import formapago


class formapagoSerializer(serializers.ModelSerializer):
    class Meta:
        model=formapago
        fields='__all__'
