from django.conf import settings
from django.db import models


class Partida(models.Model):
    JUEGOS = [
        ('oot', 'Ocarina of Time'),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='partidas',
    )
    nombre = models.CharField(max_length=100)
    juego = models.CharField(max_length=3, choices=JUEGOS, default='oot')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} ({self.get_juego_display()})'

    class Meta:
        ordering = ['-fecha_actualizacion']
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'
