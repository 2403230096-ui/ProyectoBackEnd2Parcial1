from django.shortcuts import render
from .models import Producto


def inicio(request):
    productos = Producto.objects.all()

    contexto = {
        'productos': productos,
        'total_productos': productos.count(),
    }

    return render(
        request,
        'inventario/inicio.html',
        contexto
    )