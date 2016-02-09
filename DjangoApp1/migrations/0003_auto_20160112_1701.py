# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp1', '0002_bares_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bares',
            name='direccion',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='tapas',
            name='nombre',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
