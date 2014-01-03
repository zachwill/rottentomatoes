#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import rottentomatoes

setup(name="rottentomatoes",
      version="1.1",
      description="Rotten Tomatoes Python API",
      long_description=rottentomatoes.RT.__doc__,
      keywords="rottentomatoes movies rotten tomatoes",
      author="Zach Williams",
      author_email="hey@zachwill.com",
      url="https://github.com/zachwill/rottentomatoes",
      license="Unlicense (a.k.a. Public Domain)",
      packages=["rottentomatoes"],
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'Topic :: Internet',
                   'Topic :: Internet :: WWW/HTTP',
                  ],
      test_suite="test.py",
      tests_require=["mock", "Mock"])
