from django.core.management.base import BaseCommand
from partidas.models import Categoria, Item

# Cada ítem: (nombre, archivo de imagen en public/items/)
CATALOGO = {
    'Espadas': [
        ('Practice Sword', 'SS_Practice_Sword_Icon.png'),
        ('Goddess Sword', 'SS_Goddess_Sword_Icon.png'),
        ('Goddess Longsword', 'SS_Goddess_Longsword_Icon.png'),
        ('Goddess White Sword', 'SS_Goddess_White_Sword_Icon.png'),
        ('Master Sword', 'SS_Master_Sword_Icon.png'),
        ('True Master Sowrd', 'SS_True_Master_Sword_Icon.png'),
    ],
    'Escudos': [
        ('Wooden Shield', 'SS_Wooden_Shield_Icon.png'),
        ('Banded Shield', 'SS_Banded_Shield_Icon.png'),
        ('Braced Shield', 'SS_Braced_Shield_Icon.png'),
        ('Iron Shield', 'SS_Iron_Shield_Icon.png'),
        ('Reinforced Shield', 'SS_Reinforced_Shield_Icon.png'),
        ('Fortified Shield', 'SS_Fortified_Shield_Icon.png'),
        ('Sacred Shield', 'SS_Sacred_Shield_Icon.png'),
        ('Divine Shield', 'SS_Divine_Shield_Icon.png'),
        ('Goddess Shield', 'SS_Goddess_Shield_Icon.png'),
        ('Hylian Shield', 'SS_Hylian_Shield_Icon.png'),
    ],
    'Objetos': [
        ('Honda', 'honda.png'),
        ('Escarabajo', 'escarabajo.png'),
        ('Red para insectos', 'red-para-insectos.png'),
        ('Fuelle', 'fuelle.png'),
        ('Látigo', 'latigo.png'),
        ('Arco', 'arco.png'),
        ('Garra', 'garra.png'),
        ('Bolsa de bombas', 'bolsa-de-bombas.png'),
    ],
}


class Command(BaseCommand):
    help = 'Carga el catálogo de ítems de Skyward Sword'

    def handle(self, *args, **options):
        for orden_cat, (nombre_cat, items) in enumerate(CATALOGO.items(), start=1):
            categoria, _ = Categoria.objects.get_or_create(
                nombre=nombre_cat,
                defaults={'orden': orden_cat},
            )
            for orden_item, (nombre_item, icono) in enumerate(items, start=1):
                Item.objects.update_or_create(
                    categoria=categoria,
                    nombre=nombre_item,
                    defaults={'orden': orden_item, 'icono': icono},
                )
        self.stdout.write(self.style.SUCCESS('Catálogo de Skyward Sword cargado.'))