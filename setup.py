# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__author__ = 'Viet Pham'
__copyright__ = 'Viet Pham'
__date__ = '07.08.2017'
__version__ = '0.1.0'
__status__ = 'beta'

setup(
    name='pydoo',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    version=__version__,
    description='support communication with odoo over xmlrpc api',
    author=__author__,
    author_email='dev@qvpham.com',
    url='https://github.com/julivico/pydoo',
    download_url='https://github.com/julivico/pydoo/archive/master.zip',
    keywords='python odoo xmlrpc',
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'Natural Language :: English',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: Implementation :: CPython',
                 'Programming Language :: Python :: Implementation :: PyPy'],
)
