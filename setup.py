#!/usr/bin/env python
import os
import re

from setuptools import find_packages, setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'ruia/__init__.py')) as fp:
    try:
        version = re.findall(
            r"^__version__ = \"([^']+)\"\r?$", fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        return f.read()


setup(
    name='ruia',
    version=version,
    author='Howie Hu',
    description="Ruia - An async web scraping micro-framework based on asyncio.",
    long_description=read('README.rst'),
    author_email='xiaozizayang@gmail.com',
    python_requires='>=3.6',
    install_requires=['aiohttp>=3.5.4', 'cssselect', 'lxml'],
    url="https://github.com/howie6879/ruia",
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Documentation': 'https://github.com/howie6879/ruia/blob/master/docs/index.md',
        'Source': 'https://github.com/howie6879/ruia',
    },
    extras_require={
        'uvloop': ['uvloop']
    }
)
