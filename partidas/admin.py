from django.contrib import admin
from .models import Partida


@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'juego', 'usuario', 'fecha_actualizacion')
    list_filter = ('juego',)
