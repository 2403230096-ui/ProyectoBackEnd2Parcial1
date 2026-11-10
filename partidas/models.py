from django.conf import settings
from django.db import models


class Partida(models.Model):
    JUEGOS = [
        ('ss', 'Skyward Sword'),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='partidas',
    )
    nombre = models.CharField(max_length=100)
    juego = models.CharField(max_length=3, choices=JUEGOS, default='ss', editable=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} ({self.get_juego_display()})'

    class Meta:
        ordering = ['-fecha_actualizacion']
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'


class Categoria(models.Model):
    juego = models.CharField(max_length=3, choices=Partida.JUEGOS, default='ss', editable=False)
    nombre = models.CharField(max_length=100)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f'{self.get_juego_display()} - {self.nombre}'


class Item(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='items')
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=100, blank=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['categoria__orden', 'orden']

    def __str__(self):
        return self.nombre


class ProgresoPartida(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE, related_name='progreso')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    obtenido = models.BooleanField(default=False)

    class Meta:
        unique_together = ('partida', 'item')