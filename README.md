rottentomatoes.py
================


What is this?
------------

`rottentomatoes.py` offers an easy-to-use Python wrapper to interact with the
[Rotten Tomatoes API](http://developer.rottentomatoes.com/). Before you try and
use the API, make sure you sign up to get an API Key.

In order to cut down on boilerplate code, you can then save your API key in the
`api_key_rottentomatoes.py` file.


Usage
-----

Without saving your API key:

    >>> from rottentomatoes import RT
    >>> RT('my_api_key').search('some movie here')

With your API key saved:

    >>> from rottentomatoes import RT
    >>> RT().search('some movie here')


Tests
-----

In order to run the tests for `rottentomatoes.py`, make sure you have the
[mock library](http://pypi.python.org/pypi/mock) installed.
