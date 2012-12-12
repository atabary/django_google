#!/usr/bin/env python

import google

from setuptools import setup, find_packages

setup(
    name='django_google',
    version=google.__version__,
    description='Utilities to use Google services (like Google Analytics) with Django.',
    long_description=open('README.rst').read(),
    author='Alexis Tabary',
    author_email='alexis.tabary@gmail.com',
    url='https://github.com/atabary/django_google',
    packages=find_packages(),
    license=open('LICENSE').read(),
    include_package_data=True,
    zip_safe=False,  # Django templates
    classifiers=[
        'Development Status :: 1 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
