#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from django.db import models

from common.models import NameBase


class Economy(NameBase):

    class Meta:
        verbose_name_plural = 'Economies'


class Wealth(NameBase):

    class Meta:
        verbose_name_plural = 'Wealth'

class Allegiance(NameBase):
    pass


class System(NameBase):

    allegiance = models.ForeignKey('system.Allegiance')
    economy = models.ForeignKey('system.Economy')


class StationCommodity(models.Model):

    supply = models.SmallIntegerField(choices=((-3, 'High demand'),
                                               (-2, 'Med demand'),
                                               (-1, 'Low demand'),
                                               (0, 'None'),
                                               (1, 'Low supply'),
                                               (2, 'Med supply'),
                                               (3, 'High supply')))
    synced = models.DateTimeField(auto_now=True)
    commodity = models.ForeignKey('product.Commodity')
    station = models.ForeignKey('system.Station')


class Station(NameBase):

    wealth = models.ForeignKey('system.Wealth')
    economy = models.ForeignKey('system.Economy')

    commodities = models.ManyToManyField(
        'product.Commodity',
        through='system.StationCommodity')
