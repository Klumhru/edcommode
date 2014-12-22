# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allegiance',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='economy',
            options={'verbose_name_plural': 'Economies'},
        ),
        migrations.AlterModelOptions(
            name='system',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='wealth',
            options={'verbose_name_plural': 'Wealth'},
        ),
        migrations.AddField(
            model_name='station',
            name='system',
            field=models.ForeignKey(default=1, to='system.System'),
            preserve_default=False,
        ),
        migrations.AlterOrderWithRespectTo(
            name='station',
            order_with_respect_to='system',
        ),
    ]
