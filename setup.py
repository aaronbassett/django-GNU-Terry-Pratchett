#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import gnu_terry_pratchett

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = gnu_terry_pratchett.__version__


readme = open('README.md').read()

setup(
    name='django-GNU-Terry-Pratchett',
    version=version,
    description="""You know they'll never really die while the Trunk is alive""",
    long_description=readme,
    author='Aaron Bassett',
    author_email='aaron@rawtech.io',
    url='https://github.com/aaronbassett/django-GNU-Terry-Pratchett',
    packages=[
        'gnu_terry_pratchett',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)