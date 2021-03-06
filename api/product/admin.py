#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from django.contrib import admin


from .models import Commodity


class SystemInline(admin.TabularInline):
    model = Commodity.stations.through


class CommodityAdmin(admin.ModelAdmin):
    inlines = (SystemInline,)


admin.site.register(Commodity, CommodityAdmin)
