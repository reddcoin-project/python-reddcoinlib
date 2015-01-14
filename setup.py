#!/usr/bin/env python

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README')) as f:
    README = f.read()

requires = []

setup(
    name='python-reddcoinlib',
    version='0.3.1-SNAPSHOT',
    description='This Python library provides an easy interface to the Reddcoin data structures and protocol.',
    long_description=README,

    author='Peter Todd, Larry Ren',
    author_email='pete@petertodd.org, ren@reddcoin.com',
    maintainer='Larry Ren',
    maintainer_email='ren@reddcoin.com',
    url='https://github.com/reddcoin-project/python-reddcoinlib',
    keywords='reddcoin',
    package_dir={'reddcoin': 'bitcoin'},
    packages=['reddcoin', 'reddcoin.core', 'reddcoin.tests'],
    package_data={'reddcoin.tests': ['data/*']},
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    test_suite='reddcoin.tests',
    platforms="All",
    classifiers=[
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
