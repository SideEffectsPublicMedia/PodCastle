"""
Get tag via NPR Story API.
"""

from django.conf import settings
from .story_api_get import get_dict_from_story_api

org_id = settings.STATION_ID

def get_tag(tag_id, restrict=None):
    params = {}
    params['id'] = tag_id
    params['orgId'] = org_id
    if restrict:
        params['requiredAssets'] = restrict
    return get_dict_from_story_api(params)
