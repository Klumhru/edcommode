#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from django.db import models

from common.models import NameBase


class Commodity(NameBase):

    description = models.TextField(null=True, blank=True)

    galactic_average = models.PositiveIntegerField()

    stations = models.ManyToManyField(
        'system.Station', through='system.StationCommodity')

    class Meta:
        verbose_name_plural = 'Commodities'
