#!/usr/bin/env python3
"""counterix setup.py.

This file details modalities for packaging the counterix application.
"""

from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='counterix',
    description='Generating count-based Distributional Semantic Modelss',
    author=' Alexandre Kabbach',
    author_email='akb@3azouz.net',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.0',
    url='https://github.com/akb89/counterix',
    download_url='https://github.com/akb89/counterix',
    license='MIT',
    keywords=['count-based', 'distributional semantics'],
    platforms=['any'],
    packages=['counterix', 'counterix.logging', 'counterix.exceptions',
              'counterix.utils', 'counterix.core', 'counterix.resources',
              'counterix.filtering'],
    package_data={'counterix': ['logging/*.yml', 'resources/*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'counterix = counterix.main:main'
        ],
    },
    install_requires=['pyyaml>=4.2b1'],
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Education',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Software Development :: Libraries :: Python Modules'],
    zip_safe=False,
)