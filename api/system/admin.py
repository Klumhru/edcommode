#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from django.contrib import admin

from .models import (
    System,
    Station,
    Economy,
    Allegiance,
    Wealth,
    Government,
)


class CommodityInline(admin.TabularInline):
    model = Station.commodities.through


class StationAdmin(admin.ModelAdmin):
    inlines = (CommodityInline,)


admin.site.register(System, admin.ModelAdmin)
admin.site.register(Government, admin.ModelAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Economy, admin.ModelAdmin)
admin.site.register(Allegiance, admin.ModelAdmin)
admin.site.register(Wealth, admin.ModelAdmin)
