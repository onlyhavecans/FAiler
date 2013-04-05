#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except:
    from distutils.core import setup

requires = ['beautifulsoup4', 'mechanize']

README = open('README.md').read()

setup(
    name='FAiler',
    version='0.1.0',
    description="FurAffinity Helper Library",
    url='http://github.com/tbunnyman/failer',
    author='David Aronsohn',
    author_email='tbunnyman@me.com',
    install_requires=requires,
    packages=['FAiler'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]

)
