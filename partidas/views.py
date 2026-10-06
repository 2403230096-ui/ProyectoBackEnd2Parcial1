from rest_framework import viewsets
from .models import Partida
from .serializers import PartidaSerializer


class PartidaViewSet(viewsets.ModelViewSet):
    serializer_class = PartidaSerializer

    def get_queryset(self):
        # Cada usuario solo ve sus propias partidas
        return Partida.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
