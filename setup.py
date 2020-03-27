#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = '2018-2020 CKIP Lab'
__license__ = 'CC BY-NC-SA 4.0'

import os
import sys
import warnings

from distutils.version import StrictVersion
import setuptools

assert StrictVersion(setuptools.__version__) >= StrictVersion('40.0'), \
    'Please update setuptools to 40.0+ using `pip install -U setuptools`.'

################################################################################

from setuptools import setup, find_namespace_packages
from setuptools.extension import Extension
from setuptools.command.install import install
from setuptools.command.develop import develop
from Cython.Build import cythonize

import ckipnlp as about

################################################################################

def main():

    with open('README.rst', encoding='utf-8') as fin:
        readme = fin.read()

    setup(
        name=about.__name__,
        version=about.__version__,
        author=about.__author_name__,
        author_email=about.__author_email__,
        description=about.__description__,
        long_description=readme,
        long_description_content_type='text/x-rst',
        url=about.__url__,
        download_url=about.__download_url__,
        platforms=['linux_x86_64'],
        license=about.__license__,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Cython',
            'License :: Free for non-commercial use',
            'Operating System :: POSIX :: Linux',
            'Natural Language :: Chinese (Traditional)',
        ],
        python_requires='>=3.5',
        packages=find_namespace_packages(include=['ckipnlp', 'ckipnlp.*',]),
        install_requires=[
            'treelib>=1.5.5',
        ],
        extras_require={
            'classic': ['ckip-classic>=1.0'],
            'tagger': ['ckiptagger>=0.1'],
        }
        data_files=[],
    )

################################################################################

if __name__ == '__main__':
    main()
