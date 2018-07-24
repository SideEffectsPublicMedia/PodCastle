# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from shows import models

# Register your models here.

class EpisodeInline(admin.StackedInline):
    model = models.Episode

@admin.register(models.Show)
class ShowAdmin(admin.ModelAdmin):
    inlines = [
        EpisodeInline,
    ]

@admin.register(models.Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass
