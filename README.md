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

### Methods

* `search`  -- Rotten Tomatoes movie search. Returns a list of dictionaries. Possible kwargs include: `page` and `page_limit`.
<pre><code>
    >>> rt = RT()
    >>> rt.search('the lion king')
    [{u'movie': u'here'}, {u'movie': u'here'}, ...]

    >>> rt.search('fight club', page_limit=2)
    [{'movie': 1}, {'movie': 2}]

    >>> rt.search('disney', page=2)
    [{'movie': 'from second page'}, {'movie': 'from second page'}]
</code></pre>

* `lists` -- Displays the lists available in the Rotten Tomatoes API.
<pre><code>
    >>> rt = RT()
    >>> rt.lists()
    {u'links': {u'movies': u'http://link-to-movies'
                u'dvds': u'http://link-to-dvds'}}

    >>> rt.lists('dvds')
    {u'links': {u'new_releases': u'http://link-to-new-releases'}}

    >>> rt.lists(directory='dvds')
    {u'links': {u'new_releases': u'http://link-to-new-releases'}}

    >>> rt.lists('dvds', 'new_releases')
    {u'your data': u'is right here'}

    >>> rt.lists(directory='dvds', sub='new_releases')
    {u'your data': u'is right here'}

    >>> rt.lists('movies')
    {u'links': {u'box_office': u'http://link-to-box-office-movies'},
               {u'in_theaters': u'http://link-to-movies-in-theaters'},
               {u'opening': u'http://link-to-opening-movies'},
               {u'upcoming': u'http://link-to-upcoming-movies'}}

    >>> rt.lists('movies', 'box_office')
    {u'your data': u'is right here'}

    >>> rt.lists('movies', 'box_office', page_limit=5)
    {u'only five': u'box office movies'}

    >>> rt.lists('movies', 'opening')
    {u'your data': u'is right here'}
</code></pre>

* `info` -- Return info for a movie given its `id`. Arguments for `specific_info` include `cast` and `reviews`.
<pre><code>
    >>> rt = RT()
    >>> fight_club = u'13153'
    >>> rt.info(fight_club)
    {u'your data': u'is right here'}

    >>> rt.info(fight_club, 'cast')
    {u'cast info': u'is right here'}

    >>> rt.info(fight_club, 'reviews')
    {u'reviews': u'are right here'}
</code></pre>

* `new`  -- Short method to return just opened theatrical movies or newly released dvds. Returns a list of dictionaries.
<pre><code>
    >>> rt = RT()
    >>> rt.new('movies')
    [{u'movie': u'here'}, {u'movie': u'here'}]

    >>> rt.new('dvds')
    [{u'dvd': u'here'}, {u'dvd': u'here'}]
</code></pre>

* `movies` -- Short method for returning specific movie lists. Possible sub aruments include: `box_office`, `in_theaters`, `opening`, and `upcoming`.
<pre><code>
    >>> rt = RT()
    >>> rt.movies('in_theaters', page_limit=5)
    {u'top five': u'movies in theaters'}

    >>> rt.movies('opening', page_limit=5)
    {u'top five': u'movies opening'}

    >>> rt.movies('upcoming', page=2)
    {u'page 2': u'of upcoming movies'}
</code></pre>

* `dvds` -- Short method for returning specific movie lists. Currently, only one sub argument is possible: `new_releases`.
<pre><code>
    >>> RT().dvds(page_limit=5)
    {u'only 5': u'newly released dvds'}
</code></pre>

* `feeling_lucky` -- Similar to Google's **I'm Feeling Lucky** button. Returns first instance of search term.
<pre><code>
    >>> RT().feeling_lucky('memento')
    {u'first result': u'for memento'}
</code></pre>


Tests
-----

In order to run the tests for `rottentomatoes.py`, make sure you have the
[mock library](http://pypi.python.org/pypi/mock) installed.

Also, all code complies with the [PEP 8 Style Guide](http://www.python.org/dev/peps/pep-0008/).
