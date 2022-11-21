#!/usr/bin/env python3
"""Mycounterix setup.py.

This file details modalities for packaging the Mycounterix application.
"""

from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='Mycounterix',
    description='Generating count-based Distributional Semantic Models',
    author=' Alexandre Kabbach',
    author_email='akb@3azouz.net',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='1.2.2',
    url='https://github.com/akb89/Mycounterix',
    download_url='https://github.com/akb89/Mycounterix',
    license='MIT',
    keywords=['count-based', 'distributional semantics'],
    platforms=['any'],
    packages=['Mycounterix', 'Mycounterix.logging', 'Mycounterix.exceptions',
              'Mycounterix.utils', 'Mycounterix.core'],
    package_data={'Mycounterix': ['logging/*.yml']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'Mycounterix = Mycounterix.main:main'
        ],
    },
    install_requires=['pyyaml>=4.2b1', 'scipy==1.5.1', 'embeddix==1.15.1'],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Education',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Software Development :: Libraries :: Python Modules'],
    zip_safe=False,
)
