# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp1', '0012_remove_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tapas',
            name='picture',
            field=models.FileField(upload_to='images', blank=True),
        ),
    ]
