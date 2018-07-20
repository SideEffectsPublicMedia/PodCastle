"""
Get story via NPR Story API.
"""

from django.conf import settings
from .story_api_get import get_dict_from_story_api

org_id = settings.STATION_ID

def get_story_dict(story_id):
    params = {'id': story_id}
    return get_dict_from_story_api(params)
