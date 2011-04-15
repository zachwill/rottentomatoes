rottentomatoes.py
================

<pre><code>


                      ,jf.          .K                                          
                    KKKKKKKt        KK    .                                     
                    KKK  KKK       KKKKK iK    .D,                              
                    KKK  KKK        KK,:jKKKK KKKKK                             
                    KKKtLKK.  GKK   KK  KKKKKDKK  KK ;. KKj                     
                    KKKKKKG  KKKKK .KK   KK  KKKKKKK KKKKKK                     
                    KK,,:KKKtKK fKK.KKjK KK  KK;     KK  KK                     
                    KK   KKKDKK .KK KKKL KK K KKKKKG KK  KK                     
         tD         KK   KKK KK  KK      KKKK  KKKt  KK  KK                     
 KKKKKKKKKK         KK   KKK KKKKKD       jt         KK  KK                     
 KKKKKKKKKK                   ;KK                                               
 KKKKKKK                                       KE      E                 GEE    
    :KKK                KKK: ,KKK             DKE     KKKKK.           KKKKKK.  
     KKK       D :  KKKKKKKKDKKKKK     .:    KKKKKK  :KKDKKK           KK  LEE  
     KKK   KKKKKK   KKKKKKKKKEKKKKj GKKKKKK,,KKKKKK .KKKtKtKK.         KKKKKj   
     KKK  KKKKKKK.  KKK   KKK  EKKD KKK fKKK  KK     KfttttKKL KKKKKK  KKKKKKK  
     KKK  KKKKKKKKK KKK   KKK  EKKD   :  DKK  KK    KKKDttKKK;EKKKKKKK  KKKKKKK 
     KKK. KKKKKKKKK.KKK   KKK  LKKD  DKKKKKK iKK    KKjKtKttK KKK  ;KK      KKK 
     KKKt KKKKKKKKK KKK   KKK  tKKD KKKKiKKK GKK  K.,KKKtKKKK KKKKKKKKfKKKKKKK  
     KKKE KKKKKKKKK KKK   KKK  jKKDKKK   KKK GKKLLK; jKiKKKK .KKKKKKKKD KKKKK   
     KKKK ;KKKKKKKK ,:         :;tfKKKEKKKKK  KKKKK      :    KK,               
           GKKKK                    KKKKDKKK    :             KKKEDKKK          
             KKK                                               KKKKKK           
                                                                 .i             


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

* `search` returns a list of dictionaries.
<pre><code>
    >>> rt = RT()
    >>> rt.search('the lion king')
    [{u'movie': u'here'}, {u'movie': u'here'}]
</code></pre>

* `new` can be called to return a list of either new **movies** or **dvds**.
<pre><code>
    >>> rt = RT()
    >>> rt.new('movies')
    [{u'movie': u'here'}, {u'movie': u'here'}]
</code></pre>

* `lists` can be used to search through Rotten Tomatoes API.
<pre><code>
    >>> rt = RT()
    >>> rt.lists()
    {u'links': {u'movies': u'http://link-to-movies'
                u'dvds': u'http://link-to-dvds'}

    >>> rt.lists('dvds')
    {u'links': {u'new_releases': u'http://link-to-new-releases'}

    >>> rt.lists(directory='dvds')
    {u'links': {u'new_releases': u'http://link-to-new-releases'}

    >>> rt.lists('dvds', 'new_releases')
    {u'your data': u'is right here'}

    >>> rt.lists(directory='dvds', sub='new_releases')
    {u'your data': u'is right here'}

    >>> rt.lists('dvds/new_releases')
    {'your data': u'is right here'}
</code></pre>


Tests
-----

In order to run the tests for `rottentomatoes.py`, make sure you have the
[mock library](http://pypi.python.org/pypi/mock) installed.

Also, all code complies with the [PEP 8 Style Guide](http://www.python.org/dev/peps/pep-0008/).
