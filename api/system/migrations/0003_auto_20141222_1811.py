# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20141222_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Government',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='system',
            name='government',
            field=models.ForeignKey(default=1, to='system.Government'),
            preserve_default=False,
        ),
    ]
