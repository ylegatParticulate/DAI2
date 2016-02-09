# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp1', '0009_tapas_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tapas',
            old_name='likes',
            new_name='num_visitas',
        ),
    ]
