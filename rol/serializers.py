from rest_framework import serializers
from rol.models import rol


class rolSerializer(serializers.ModelSerializer):
    class Meta:
        model=rol
        fields='__all__'

