# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20141222_1811'),
        ('product', '0002_auto_20141222_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='systems',
            field=models.ManyToManyField(to='system.Station', through='system.StationCommodity'),
            preserve_default=True,
        ),
    ]
