# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp1', '0007_pagecounter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PageCounter',
        ),
    ]
