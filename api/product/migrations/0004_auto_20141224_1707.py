# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_commodity_systems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commodity',
            old_name='systems',
            new_name='stations',
        ),
    ]
