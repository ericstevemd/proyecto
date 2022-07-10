from rest_framework import serializers
from producto.models import tipoDocumento


class tipodocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=tipoDocumento
        fields='__all__'

