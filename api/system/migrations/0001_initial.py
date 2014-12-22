# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allegiance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Economy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StationCommodity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supply', models.SmallIntegerField(choices=[(-3, 'High demand'), (-2, 'Med demand'), (-1, 'Low demand'), (0, 'None'), (1, 'Low supply'), (2, 'Med supply'), (3, 'High supply')])),
                ('synced', models.DateTimeField(auto_now=True)),
                ('commodity', models.ForeignKey(to='product.Commodity')),
                ('station', models.ForeignKey(to='system.Station')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('allegiance', models.ForeignKey(to='system.Allegiance')),
                ('economy', models.ForeignKey(to='system.Economy')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wealth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='station',
            name='commodities',
            field=models.ManyToManyField(to='product.Commodity', through='system.StationCommodity'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='station',
            name='economy',
            field=models.ForeignKey(to='system.Economy'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='station',
            name='wealth',
            field=models.ForeignKey(to='system.Wealth'),
            preserve_default=True,
        ),
    ]
