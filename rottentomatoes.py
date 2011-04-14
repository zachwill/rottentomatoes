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

    def __init__(self, api_key='', version=1.0):
        if not api_key:
            self.api_key = API_KEY
        else:
            self.api_key = api_key
        self.BASE_URL = 'http://api.rottentomatoes.com/api/public/v%s/' %\
                str(version)  # Python has quirky float behavior
        self.lists_url = self.BASE_URL + 'lists'
        self.search_url = self.BASE_URL + 'movies?'

    def search(self, query, page=1, page_limit=30):
        """Rotten Tomatoes movie search endpoint."""
        params = urlencode({'apikey': self.api_key, 'q': query, 'page': page,
            'page_limit': page_limit})
        url = self.search_url + params
        data = json.loads(urllib2.urlopen(url).read())
        return data

    def lists(self, directory=None, sub=None):
        """
        Displays the lists available in the Rotten Tomatoes API.

        Example usage:

        >>> RT().lists()
        {u'links': {u'movies': u'http://link-to-movies'
                    u'dvds': u'http://link-to-dvds'}
        >>> RT().lists('dvds')
        {u'links': {u'new_releases': u'http://link-to-new-releases'}
        >>> RT().lists(directory='dvds')
        {u'links': {u'new_releases': u'http://link-to-new-releases'}
        >>> RT().lists('movies', 'upcoming')
        {'your data':'right here'}
        >>> RT().lists(directory='movies', sub='upcoming')
        {'your data':'right here'}
        """
        lists_url = self.lists_url
        if directory:
            if sub:
                lists_url += '/%s/%s' % (directory, sub)
            else:
                lists_url += '/%s' % directory
        lists_url += '.json?'
        params = urlencode({'apikey': self.api_key})
        lists_url += params
        data = json.loads(urllib2.urlopen(lists_url).read())
        return data
