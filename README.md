rottentomatoes.py
================

`rottentomatoes` offers an easy-to-use Python wrapper to interact with the
[Rotten Tomatoes API](http://developer.rottentomatoes.com/). Before you try and
use the API, make sure you sign up to get an API Key.


Installation
------------

If you have `pip` installed, then run the following command:

    pip install rottentomatoes

You can also run `easy_install`:

    easy_install rottentomatoes

Or, if you want to help develop the package, just `git clone` the Github
repository:

    git clone https://github.com/zachwill/rottentomatoes.git


Usage
-----

Without saving your API key as a `RT_KEY` environment variable:

```python
from rottentomatoes import RT

RT('my_api_key').search('some movie here')
```

With your API key saved:

```python
from rottentomatoes import RT

RT().search('some movie here')
```

**NOTE**: Documentation from this point forward will assume you have saved your
Rotten Tomatoes Developer API Key as a `RT_KEY` environment variable:

    $ RT_KEY='my_api_key'
    $ echo $RT_KEY


Methods
-------

### `search`

Rotten Tomatoes movie search. Returns a list of dictionaries. Possible keyword arguments include: `page` and `page_limit`.

```python
>>> rt = RT()
>>> rt.search('the lion king')
[{'movie': 'here'}, {'movie': 'here'}, ...]

>>> rt.search('fight club', page_limit=2)
[{'movie': 1}, {'movie': 2}]

>>> rt.search('disney', page=2)
[{'movie': 'from second page'}, {'movie': 'from second page'}, ...]
```

### `lists`

Displays the lists available in the Rotten Tomatoes API.

```python
>>> rt = RT()
>>> rt.lists()
{'links': {'movies': 'http://link-to-movies',
           'dvds': 'http://link-to-dvds'}}

>>> rt.lists('dvds')
{'links': {'new_releases': 'http://link-to-new-releases'}}

>>> rt.lists(directory='dvds')
{'links': {'new_releases': 'http://link-to-new-releases'}}

>>> rt.lists('dvds', 'new_releases')
{'your data': 'is right here'}

>>> rt.lists(directory='dvds', sub='new_releases')
{'your data': 'is right here'}

>>> rt.lists('movies')
{'links': {'box_office': 'http://link-to-box-office-movies',
           'in_theaters': 'http://link-to-movies-in-theaters',
           'opening': 'http://link-to-opening-movies',
           'upcoming': 'http://link-to-upcoming-movies'}

>>> rt.lists('movies', 'box_office')
{'your data': 'is right here'}

>>> rt.lists('movies', 'box_office', page_limit=5)
{'only five': 'box office movies'}

>>> rt.lists('movies', 'opening')
{'your data': 'is right here'}
```

### `info`

Return info for a movie given its `id`. Arguments for `specific_info` include `cast` and `reviews`.

```python
>>> rt = RT()
>>> fight_club = '13153'
>>> rt.info(fight_club)
{'your data': 'is right here'}

>>> rt.info(fight_club, 'cast')
{'cast info': 'is right here'}

>>> rt.info(fight_club, 'reviews')
{'reviews': 'are right here'}
```

### `new`

Short method to return just opened theatrical movies or newly released dvds. Returns a list of dictionaries.

```python
>>> rt = RT()
>>> rt.new('movies')
[{'movie': 'here'}, {'movie': 'here'}, ...]

>>> rt.new('dvds')
[{'dvd': 'here'}, {'dvd': 'here'}, ...]
```

### `movies`

Short method for returning specific movie lists. Possible `sub` arguments include: `box_office`, `in_theaters`, `opening`, and `upcoming`.

```python
>>> rt = RT()
>>> rt.movies('in_theaters', page_limit=5)
{'top five': 'movies in theaters'}

>>> rt.movies('opening', page_limit=5)
{'top five': 'movies opening'}

>>> rt.movies('upcoming', page=2)
{'page 2': 'of upcoming movies'}
```python

* `dvds` -- Short method for returning specific dvd lists. Currently, only one `sub` argument is possible: `new_releases`.
```python
>>> RT().dvds(page_limit=5)
{'only 5': 'newly released dvds'}
```

### `feeling_lucky`

Similar to Google's **I'm Feeling Lucky** button. Returns first instance of search term.

```python
>>> RT().feeling_lucky('memento')
{'first result': 'for memento'}
```

Tests
-----

In order to run the tests for `rottentomatoes.py`, make sure you have the
[mock library](http://pypi.python.org/pypi/mock) installed.

Also, all code complies with the [PEP 8 Style Guide](http://www.python.org/dev/peps/pep-0008/).


License
-------

**Author**: Zach Williams

All code released under [the Unlicense](http://unlicense.org/) (a.k.a. Public Domain).
