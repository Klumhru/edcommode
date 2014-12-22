#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from django.db import models


class NameBase(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ('name',)
