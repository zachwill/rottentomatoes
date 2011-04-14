#!/usr/bin/env python

"""Unit tests for the `rottentomatoes.py` file."""

import unittest
from urlparse import urlparse, parse_qs
from mock import Mock
import rottentomatoes
from rottentomatoes import RT


class TestApiKey(unittest.TestCase):

    def setUp(self):
        """
        Mock the urllib2 and json libraries in the `rottentomatoes.py` file.
        Makes for fast unit tests.
        """
        rottentomatoes.urllib2.urlopen = Mock()
        rottentomatoes.json = Mock()
        rottentomatoes.API_KEY = 'my_api_key'

    def test_rottentomatoes_api_key(self):
        self.assertEqual(RT().api_key, 'my_api_key')

    def test_rottentomateos_called_api_key(self):
        self.assertEqual(RT('called_api_key').api_key, 'called_api_key')


class TestCorrectSearchUrl(unittest.TestCase):

    def setUp(self):
        rottentomatoes.urllib2.urlopen = Mock()
        rottentomatoes.json = Mock()
        rottentomatoes.API_KEY = 'my_api_key'

    def test_empty_search_url_keys(self):
        RT().search('')
        call = rottentomatoes.urllib2.urlopen.call_args[0][0]
        query = urlparse(call).query
        movie = parse_qs(query)
        self.assertEqual(movie.keys(), ['apikey', 'page', 'page_limit'])

    def test_nonempty_search_url_keys(self):
        RT().search('some movie')
        call = rottentomatoes.urllib2.urlopen.call_args[0][0]
        query = urlparse(call).query
        movie = parse_qs(query)
        self.assertEqual(movie.keys(), ['q', 'apikey', 'page', 'page_limit'])

    def test_search_url_for_lion_king(self):
        RT().search('the lion king')
        call = rottentomatoes.urllib2.urlopen.call_args[0][0]
        query = urlparse(call).query
        movie = parse_qs(query)
        assert 'my_api_key' in movie['apikey']
        assert 'the lion king' in movie['q']

    def test_search_url_for_ronin(self):
        RT().search('ronin')
        call = rottentomatoes.urllib2.urlopen.call_args[0][0]
        query = urlparse(call).query
        movie = parse_qs(query)
        assert 'my_api_key' in movie['apikey']
        assert 'ronin' in movie['q']


if __name__ == '__main__':
    unittest.main()
