from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'precio',
        'cantidad',
        'fecha_registro',
    )

    search_fields = ('nombre', 'descripcion')

    list_filter = ('fecha_registro',)

    list_per_page = 10