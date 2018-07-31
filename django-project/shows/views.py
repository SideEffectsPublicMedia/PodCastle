# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bakery.views import BuildableDetailView
from django.shortcuts import render
from .models import *

# Create your views here.

class ShowDetailView(BuildableDetailView):
    model = Show
    template_name = 'shows/show_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Show.objects.get(slug=self.kwargs['slug'])
        return super(ShowDetailView, self).get_object()

class EpisodeDetailView(BuildableDetailView):
    model = Episode
    template_name = 'shows/episode_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Episode.objects.get(story_api_id=self.kwargs['slug'])
        return super(EpisodeDetailView, self).get_object()
