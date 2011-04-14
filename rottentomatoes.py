#!/usr/bin/env python

"""
Rotten Tomatoes API:  http://developer.rottentomatoes.com/

Main file for interacting with the Rotten Tomatoes API.
"""

import urllib2
from api_key_rottentomatoes import API_KEY

class RT(object):

    def __init__(self, api_key=''):
        if not api_key:
            self.api_key = API_KEY
        else:
            self.api_key = api_key
