#!/usr/bin/env python3

from setuptools import setup

setup(
    name='downloader',
    version='0.0.1',
    description='http file downloader',
    author='Andrew Dorokhin (@andrewnsk)',
    author_email='andrew@dorokhin.moscow',
    url='http://github.com/andrewnsk/downloader',
    packages=['downloader', 'tests.unit'],
    long_description="""\
      http file downloader
      """,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    package_data={
        '': ['*.txt', '*.xsd']
    },
    keywords='download http',
    license='MIT',
    test_suite='tests'
)
