#!/usr/bin/env python

from setuptools import find_packages, setup
from cmsplugin_tabs import VERSION

setup(
    name='cmsplugin-tabs',
    version=VERSION,
    author='Tomas Neme',
    author_email='lacrymology@gmail.com',
    url='http://github.com/Lacrymology',
    description = ('django-cms plugin to help rendering things like tabs or '
                   'accordion widgets'),
    packages=find_packages(),
    provides=['cmsplugin_tabs', ],
    include_package_data=True,
    install_requires = [
        'django-inline-ordering>=0.1.1',
        'django-sekizai',
        ],
)
