rottentomatoes.py
================

<pre><code>


                      ,jf.          .K                                          
                    KKKKKKKt        iK    .                                     
                    KKK  KKK       KKKKK iK    .D,                              
                    KKK  KKK        KK,:jKKKK KKKKK                             
                    KKKtLKK.  GKK   KK  KKKKKDKK  KK ;. KKj                     
                    KKKKKKG  KKKKK .KK   KK  KKKKKKK KKKKKK                     
                    KK,,:KKKtKK fKK.KKjK KK  KK;     KK  KK                     
                    KK   KKKDKK .KK KKKL KK K KKKKKG KK  KK                     
                    KK   KKK KK  KK      KKKK  KKKt  KK  KK                     
 KKKKKKKKKK         KK   KKK KKKKKD       jt         KK  KK                     
 KKKKKKKKKK                   ;KK                                               
 KKKKKKKKKK                                    KE                        GEE    
    :KKK                KKK: ,KKK             DKE     KKKKK.           KKKKKK.  
     KKK       D :  KKKKKKKKDKKKKK           KKKKKK  :KKDKKK           KK  LEE  
     KKK   KKKKKK   KKKKKKKKKEKKKKj GKKKKKK,,KKKKKK .KKKtKtKK.         KKKKKj   
     KKK  KKKKKKK.  KKK   KKK  EKKD KKK fKKK  KK     KfttttKKL KKKKKK  KKKKKKK  
     KKK  KKKKKKKKK KKK   KKK  EKKD      DKK  KK    KKKDttKKK;EKKKKKKK  KKKKKKK 
     KKK. KKKKKKKKK.KKK   KKK  LKKD  DKKKKKK iKK    KKjKtKttK KKK  ;KK      KKK 
     KKKt KKKKKKKKK KKK   KKK  tKKD KKKKiKKK GKK  K.,KKKtKKKK KKKKKKKKfKKKKKKK  
     KKKE KKKKKKKKK KKK   KKK  jKKDKKK   KKK GKKLLK; jKiKKKK .KKKKKKKKD KKKKK   
     KKKK ;KKKKKKKK              tfKKKEKKKKK  KKKKK           KK,               
           GKKKK                    KKKKDKKK                  KKKEDKKK          
             KKK                                               KKKKKK           



                   https://github.com/zachwill/rottentomatoes

</code></pre>


Changelog
---------

### 1.1
 * Support `gzip`-encoded responses from the API (thanks to [`devrelm`](https://github.com/devrelm))

### 1.0.1
 * 100% test coverage.
 * Removal of all `+=` operators -- now using `''.join()` instead.

### 1.0
 * Initial release.


What is this?
------------

`rottentomatoes` offers an easy-to-use Python wrapper to interact with the
[Rotten Tomatoes API](http://developer.rottentomatoes.com/). Before you try and
use the API, make sure you sign up to get an API Key.

In order to cut down on boilerplate code, you can then save your API key in the
`rottentomatoes_api_key.py` file.

Also, note that this package is in no way associated or endorsed by
[RottenTomatoes.com](http://www.rottentomatoes.com/) or [Flixster,
Inc](http://www.flixster.com/).


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

Without saving your API key in the `rottentomatoes_api_key.py` file:

    >>> from rottentomatoes import RT
    >>> RT('my_api_key').search('some movie here')

With your API key saved:

    >>> from rottentomatoes import RT
    >>> RT().search('some movie here')

**NOTE**: Documentation from this point forward will assume you have saved your
Rotten Tomatoes Developer API Key to the `rottentomatoes_api_key.py` file (which
you should consider doing in order to cut down on boilerplate code).


### Methods

* `search`  -- Rotten Tomatoes movie search. Returns a list of dictionaries. Possible kwargs include: `page` and `page_limit`.
<pre><code>
    >>> rt = RT()
    >>> rt.search('the lion king')
    [{'movie': 'here'}, {'movie': 'here'}, ...]

    >>> rt.search('fight club', page_limit=2)
    [{'movie': 1}, {'movie': 2}]

    >>> rt.search('disney', page=2)
    [{'movie': 'from second page'}, {'movie': 'from second page'}, ...]
</code></pre>

* `lists` -- Displays the lists available in the Rotten Tomatoes API.
<pre><code>
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
</code></pre>

* `info` -- Return info for a movie given its `id`. Arguments for `specific_info` include `cast` and `reviews`.
<pre><code>
    >>> rt = RT()
    >>> fight_club = '13153'
    >>> rt.info(fight_club)
    {'your data': 'is right here'}

    >>> rt.info(fight_club, 'cast')
    {'cast info': 'is right here'}

    >>> rt.info(fight_club, 'reviews')
    {'reviews': 'are right here'}
</code></pre>

* `new`  -- Short method to return just opened theatrical movies or newly released dvds. Returns a list of dictionaries.
<pre><code>
    >>> rt = RT()
    >>> rt.new('movies')
    [{'movie': 'here'}, {'movie': 'here'}, ...]

    >>> rt.new('dvds')
    [{'dvd': 'here'}, {'dvd': 'here'}, ...]
</code></pre>

* `movies` -- Short method for returning specific movie lists. Possible `sub` arguments include: `box_office`, `in_theaters`, `opening`, and `upcoming`.
<pre><code>
    >>> rt = RT()
    >>> rt.movies('in_theaters', page_limit=5)
    {'top five': 'movies in theaters'}

    >>> rt.movies('opening', page_limit=5)
    {'top five': 'movies opening'}

    >>> rt.movies('upcoming', page=2)
    {'page 2': 'of upcoming movies'}
</code></pre>

* `dvds` -- Short method for returning specific dvd lists. Currently, only one `sub` argument is possible: `new_releases`.
<pre><code>
    >>> RT().dvds(page_limit=5)
    {'only 5': 'newly released dvds'}
</code></pre>

* `feeling_lucky` -- Similar to Google's **I'm Feeling Lucky** button. Returns first instance of search term.
<pre><code>
    >>> RT().feeling_lucky('memento')
    {'first result': 'for memento'}
</code></pre>


Tests
-----

In order to run the tests for `rottentomatoes.py`, make sure you have the
[mock library](http://pypi.python.org/pypi/mock) installed.

Also, all code complies with the [PEP 8 Style Guide](http://www.python.org/dev/peps/pep-0008/).


License
-------

**Author**: Zach Williams

All code released under [the Unlicense](http://unlicense.org/) (a.k.a. Public
Domain).
