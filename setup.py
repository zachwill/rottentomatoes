#!/usr/bin/env python

from distutils.core import setup

setup(name="rottentomatoes",
      version="1.0",
      description="Rotten Tomatoes Python API",
      keywords="rottentomatoes movies rotten tomatoes",
      author="Zach Williams",
      author_email="hey@zachwill.com",
      url="https://github.com/zachwill/rottentomatoes",
      license="Public Domain",
      py_modules=["rottentomatoes.py", "rottentomatoes_api_key.py"],
      test_suite="test.py",
      tests_require=["mock", "Mock"],
      repository_url="https://github.com/zachwill/rottentomatoes")
