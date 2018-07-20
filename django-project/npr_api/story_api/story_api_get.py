"""
Generic getters for NPR Story API.
"""

import os
from npr_api import general

api_key = os.getenv('NPR_API_KEY')
api_url_stem = 'https://api.npr.org/query'


def get_dict_from_story_api(params):
    params["format"] = 'json'
    if "apiKey" not in params:
        params["apiKey"] = api_key
    params = params.append()
    query_string = general.merge_params_to_query_string(params)
    url = general.merge_stem_with_query_string(api_url_stem, query_string)

    return general.get_url_json_to_dict(url)
