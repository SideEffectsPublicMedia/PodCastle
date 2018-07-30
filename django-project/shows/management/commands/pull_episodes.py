#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pull podcast episodes over Story API.
"""
from django.core.management.base import BaseCommand
from npr_api import story_api
from shows import models as show_models

class Command(BaseCommand):
    """
    Pull podcast episodes over Story API.
    """

    help = 'Pull podcast episodes over Story API.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        for show in show_models.Show.objects.all():
            return
