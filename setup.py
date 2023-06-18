#!/usr/bin/env python3

from distutils.core import setup

setup(name='elecsys',
      version='0.1.0',
      description='Electoral systems',
      url='https://github.com/moerbeke/elecsys',
      author='Antonio Ceballos Roa',
      author_email='aceballos@gmail.com',
      packages=['elecsys'],
      scripts=['compute-seats.py'],
      license='GPLv3+',
     )
