import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')

import django
django.setup()

from DjangoApp1.models import Bares, Tapas


def populate():
    nuevo_bar = add_bar('Bar 1','Bar2','Bar3')

    add_tapa(bar=nuevo_bar,
        nombre='Pizza')

    add_tapa(bar=nuevo_bar,
        nombre='Bocadillo de jamon')

    add_tapa(bar=nuevo_bar,
        nombre='Jamon York con queso')


    nuevo_bar= add_bar('Bar 4', 'Bar5')

    add_tapa(bar=nuevo_bar,
        nombre='salmón')

    add_tapa(bar=nuevo_bar,
        nombre='Tapa aleman')

    add_tapa(bar=nuevo_bar,
        nombre='Tapa italiano')


    # Print out what we have added to the user.
    for b in Bares.objects.all():
        for t in Tapas.objects.filter(bar=b):
            print("- {0} - {1}".format(str(b), str(t)))

def add_tapa(bar, nombre):
    t = Tapas.objects.get_or_create(bar=bar, nombre=nombre)[0]
    t.bar=bar
    t.nombre=nombre
    t.votos=votos
    t.likes=likes
    t.save()
    return t

def add_bar(nombre, direccion):
    b = Bares.objects.get_or_create(nombre=nombre, direccion=direccion,num_visitas=num_visitas)[0]
    b.likes=likes
    b.save()
    return b

# Start execution here!
if __name__ == '__main__':
    print("Starting DjangoApp population script...")
    populate()
