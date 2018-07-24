# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Show (models.Model):
    slug = models.SlugField(max_length=250,
                            unique=True)
    name = models.CharField(max_length=512)
    story_api_tag_id = models.CharField(
        "NPR Story API Tag ID",
        help_text="Used to pull in episodes. \
        Consult NPR Digital to get this activated on your site.",
        max_length=150)
    story_api_org_id = models.CharField(
        "NPR Story API Org ID",
        help_text="Your OrgID for the NPR Story API. \
                  Without this, the tool will be unable to pull in episodes.",
        max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to="shows/images")
    custom_banner = models.FileField(upload_to="shows/banners",
                                     blank=True,
                                     null=True)
    feed_url = models.URLField(
        "Podcast (RSS) Feed URL",
        max_length=1024,
        null=True,
        blank=True)
    itunes_url = models.URLField(
        "Apple Podcasts/iTunes Page URL",
        max_length=1024,
        null=True,
        blank=True)
    stitcher_url = models.URLField(
        "Stitcher Page URL",
        max_length=1024,
        null=True,
        blank=True)
    google_url = models.URLField(
        "Google Play Podcasts Page URL",
        max_length=1024,
        null=True,
        blank=True)
    overcast_url = models.URLField(
        "Overcast Page URL",
        max_length=1024,
        null=True,
        blank=True)
    pocket_casts_url = models.URLField(
        "Pocket Casts Page URL",
        max_length=1024,
        null=True,
        blank=True)
    npr_one_url = models.URLField(
        "NPR One URL",
        max_length=1024,
        null=True,
        blank=True)


    class Meta:
        ordering = ['slug']

    def get_absolute_url(self):
        return "/{}/".format(self.slug)

    def __str__(self):
        return "%s" % self.name

class Episode(models.Model):
    story_api_id = models.CharField(
                                    "Story API ID",
                                    max_length=512,
                                    unique=True)
    name = models.CharField(max_length=512)
    date = models.DateField()
    image_url = models.URLField("Featured Image URL", max_length=1024)
    audio_url = models.URLField("MP3 File URL", max_length=1024)
    show = models.ForeignKey(Show, related_name='episodes')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/{}/{}/".format(self.show.slug, self.story_api_id)
