# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp1', '0005_userprofile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='bares',
            name='visits_bar',
            field=models.IntegerField(default=0),
        ),
    ]
