#!/usr/bin/env python

"""Unit tests for the `rottentomatoes.py` file."""

import unittest
from urlparse import urlparse, parse_qs
from mock import Mock
import rottentomatoes
from rottentomatoes import RT


def set_up():
    """
    Mock both urllib2 and json.loads return value. Makes for fast unit tests.
    """
    rottentomatoes.urllib2.urlopen = Mock()
    rottentomatoes.json.loads = Mock(return_value={'movies': []})
    rottentomatoes.API_KEY = 'my_api_key'


def call_args(kind='query'):
    """Find out what urllib2.urlopen called while mocking."""
    call = rottentomatoes.urllib2.urlopen.call_args[0][0]
    parsed = urlparse(call)
    if kind == 'query':
        return  parse_qs(parsed.query)
    elif kind == 'path':
        return parsed.path


class ApiKeyTest(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_rottentomatoes_api_key(self):
        self.assertEqual(RT().api_key, 'my_api_key')

    def test_rottentomateos_called_api_key(self):
        self.assertEqual(RT('called_api_key').api_key, 'called_api_key')


class SearchUrlTest(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_empty_search_url_keys(self):
        RT().search('')
        movie = call_args()
        self.assertEqual(movie.keys(), ['apikey', 'page', 'page_limit'])

    def test_nonempty_search_url_keys(self):
        RT().search('some movie')
        movie = call_args()
        self.assertEqual(movie.keys(), ['q', 'apikey', 'page', 'page_limit'])

    def test_nonempty_search_url_path(self):
        RT().search('some movie')
        path = call_args('path')
        self.assertEqual(path, '/api/public/v1.0/movies')

    def test_search_url_for_lion_king(self):
        RT().search('the lion king')
        movie = call_args()
        assert 'my_api_key' in movie['apikey']
        assert 'the lion king' in movie['q']

    def test_search_url_for_ronin(self):
        RT().search('ronin')
        movie = call_args()
        assert 'my_api_key' in movie['apikey']
        assert 'ronin' in movie['q']


class ListsUrlTest(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_empty_lists_url_path(self):
        RT().lists()
        path = call_args('path')
        self.assertEqual(path, '/api/public/v1.0/lists.json')

    def test_lists_url_path_for_dvds(self):
        RT().lists('dvds')
        path = call_args('path')
        self.assertEqual(path, '/api/public/v1.0/lists/dvds.json')

    def test_lists_url_path_for_dvds_sub_new_releases(self):
        RT().lists('dvds', 'new_releases')
        path = call_args('path')
        self.assertEqual(path, '/api/public/v1.0/lists/dvds/new_releases.json')

    def test_lists_url_path_for_movies(self):
        RT().lists('movies')
        path = call_args('path')
        self.assertEqual(path, '/api/public/v1.0/lists/movies.json')

    def test_lists_url_path_for_movies_sub_opening(self):
        RT().lists('movies', 'opening')
        path = call_args('path')
        self.assertEqual(path, '/api/public/v1.0/lists/movies/opening.json')

    def test_lists_url_keys_for_extra_kwargs(self):
        RT().lists('movies', 'in_theaters', limit=5)
        parsed_query = call_args()
        assert 'my_api_key' in parsed_query['apikey']
        assert '5' in parsed_query['limit']


class NewUrlTest(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_new_url_path_for_dvds(self):
        RT().new('dvds')
        path = call_args('path')
        self.assertEqual(path, '/api/public/v1.0/lists/dvds/new_releases.json')

    def test_new_url_keys_for_dvds_with_kwargs(self):
        RT().new('movies', page=2)
        parsed_query = call_args()
        assert '2' in parsed_query['page']

    def test_new_url_path_for_movies(self):
        RT().new('movies')
        path = call_args('path')
        self.assertEqual(path, '/api/public/v1.0/lists/movies/opening.json')

    def test_new_url_keys_for_movies_with_kwargs(self):
        RT().new('movies', page_limit=5)
        parsed_query = call_args()
        assert '5' in parsed_query['page_limit']


if __name__ == '__main__':
    unittest.main()
