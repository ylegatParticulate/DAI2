# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp1', '0010_auto_20160119_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tapas',
            old_name='num_visitas',
            new_name='likes',
        ),
        migrations.AddField(
            model_name='bares',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
