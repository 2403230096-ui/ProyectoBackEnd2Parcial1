from rest_framework import serializers
from .models import Partida


class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = ['id', 'nombre', 'juego', 'fecha_creacion', 'fecha_actualizacion']
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']
