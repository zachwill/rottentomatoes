#!/usr/bin/env python

"""
Rotten Tomatoes API:  http://developer.rottentomatoes.com/

Main file for interacting with the Rotten Tomatoes API.
"""

import urllib2
from urllib import urlencode
try:
    import json
except ImportError:
    import simplejson as json

from api_key_rottentomatoes import API_KEY

class RT(object):
    """
    An easy-to-use Python wrapper for the Rotten Tomatoes API.

    Usage:

    >>> RT('my-api-key').search('the lion king')

    Or, if your API key is stored in the `api_key_rottentomatoes.py` file,
    the RT class can be initialized like so:

    >>> RT().search('the lion king')
    """

    def __init__(self, api_key=''):
        if not api_key:
            self.api_key = API_KEY
        else:
            self.api_key = api_key
        BASE_URL = 'http://api.rottentomatoes.com/api/public/v1.0/'
        self.list_url = ''.join([BASE_URL, 'lists.json?apikey=', self.api_key])
        self.search_url = ''.join([BASE_URL, 'movies?apikey=',
            self.api_key, '&'])

    def search(self, query, page=1, page_limit=30):
        """Rotten Tomatoes movie search endpoint."""
        q = urlencode({'q': query, 'page': page, 'page_limit': page_limit})
        url = self.search_url + q
        data = json.loads(urllib2.urlopen(url).read())
        return data
