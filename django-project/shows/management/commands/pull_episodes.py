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

        episodes_scraped = 0
        episodes_added = 0

        for show in show_models.Show.objects.all():
            tag = story_api.ApiTag(
                tag_id=show.story_api_tag_id,
                org_id=show.story_api_org_id,
                restrict="image,audio"
            )

            for api_story in tag.stories:
                _episode, created = show_models.Episode.objects.update_or_create(
                    story_api_id=api_story.story_id,
                    show=show,
                    defaults={
                        "text": api_story.html_text,
                        "name": api_story.title,
                        "audio_url": api_story.audio["url"],
                        "date": api_story.date_time,
                        "image_url": api_story.image["url"],
                        "image_caption": api_story.image["caption"],
                        "image_alt": api_story.image["alt"],
                        "image_credit": api_story.image["author"],
                        "image_source": api_story.image["source"],
                        "canonical_url": api_story.canonical_link,
                    }
                )
                if created:
                    episodes_added += 1
                episodes_scraped += 1

        print("Shows scraped: {}. Shows added: {}.".format(episodes_scraped, episodes_added))
