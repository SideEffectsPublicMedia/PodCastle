"""
JSON request tools for all APIs.
"""

import requests
import json

def get_url_json_to_dict(url):
    """

    Generalized JSON request tool that returns dict.

    :param url: API JSON endpoint
    :return: A dictionary of results.
    """
    r = requests.get(url)
    json_data = r.json()
    return json_data
