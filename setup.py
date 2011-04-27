#!/usr/bin/env python

from distutils.core import setup
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
VERSION = file(os.path.join(PROJECT_ROOT, 'VERSION')).read().strip()

setup(name='Django Pro History',
      version=VERSION,
      description='Adds generic history support for models',
      author='Marthy Alchin with some updates by Luca Ferroni',
      author_email='fero@jagom.org',
      url='https://github.com/feroda/django-pro-history',
      packages=['history', 'current_user'],
     )

