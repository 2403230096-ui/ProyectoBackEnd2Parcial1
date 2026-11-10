from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Partida, Categoria, Item, ProgresoPartida
from .serializers import PartidaSerializer


class PartidaViewSet(viewsets.ModelViewSet):
    serializer_class = PartidaSerializer

    def get_queryset(self):
        # Cada usuario solo ve sus propias partidas
        return Partida.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    @action(detail=True, methods=['get'], url_path='tracker')
    def tracker(self, request, pk=None):
        partida = get_object_or_404(Partida, pk=pk, usuario=request.user)
        obtenidos = set(
            ProgresoPartida.objects.filter(partida=partida, obtenido=True)
            .values_list('item_id', flat=True)
        )

        categorias = []
        total = 0
        total_obtenidos = 0
        for cat in Categoria.objects.filter(juego=partida.juego).prefetch_related('items'):
            items = []
            for it in cat.items.all():
                ok = it.id in obtenidos
                items.append({'id': it.id, 'nombre': it.nombre,'icono': it.icono, 'obtenido': ok})
                total += 1
                total_obtenidos += ok
            categorias.append({'id': cat.id, 'nombre': cat.nombre, 'items': items})

        porcentaje = round(total_obtenidos * 100 / total) if total else 0
        return Response({'categorias': categorias, 'porcentaje': porcentaje})

    @action(
        detail=True, methods=['post'],
        url_path=r'items/(?P<item_id>[0-9]+)/toggle',
    )
    def toggle_item(self, request, pk=None, item_id=None):
        partida = get_object_or_404(Partida, pk=pk, usuario=request.user)
        item = get_object_or_404(Item, pk=item_id)
        progreso, _ = ProgresoPartida.objects.get_or_create(partida=partida, item=item)
        progreso.obtenido = not progreso.obtenido
        progreso.save()
        partida.save(update_fields=['fecha_actualizacion'])
        return Response({'item': item.id, 'obtenido': progreso.obtenido})