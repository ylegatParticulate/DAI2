# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp1', '0008_delete_pagecounter'),
    ]

    operations = [
        migrations.AddField(
            model_name='tapas',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
