#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djangocms_button

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_button.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()

setup(
    name='djangocms-button',
    version=version,
    description='Button plugin for django CMS',
    long_description=readme,
    author='Digital Anvil',
    author_email='webmaster@digitalanvil.co.uk',
    url='https://github.com/digital-anvil/djangocms-button',
    packages=[
        'djangocms_button',
    ],
    include_package_data=True,
    install_requires=[
        'django-cms >= 3.0',
        'django-appconf >= 1.0.1',
        'django >= 1.7',
        'django-select2>=4.3',
    ],
    license="BSD",
    zip_safe=False,
    keywords=[
        'django', 'cms', 'link', 'button'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
