#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from django.contrib import admin


from .models import Commodity

admin.site.register(Commodity, admin.ModelAdmin)
