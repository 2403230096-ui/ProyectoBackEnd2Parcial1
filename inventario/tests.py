from django.test import TestCase
from .models import Producto


class ProductoTestCase(TestCase):

    def test_crear_producto(self):
        producto = Producto.objects.create(
            nombre='Teclado',
            descripcion='Teclado mecánico',
            precio=850.00,
            cantidad=10
        )

        self.assertEqual(producto.nombre, 'Teclado')
        self.assertEqual(producto.precio, 850.00)
        self.assertEqual(producto.cantidad, 10)

    def test_consultar_producto(self):
        Producto.objects.create(
            nombre='Mouse',
            precio=350.00,
            cantidad=5
        )

        producto = Producto.objects.get(nombre='Mouse')

        self.assertEqual(producto.cantidad, 5)