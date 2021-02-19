#!/usr/bin/env python
"""The setup script."""

from setuptools import setup, find_packages
import perry_bot as module
import os


def walker(base, *paths):
    """Finds package data.."""
    file_list = set()
    cur_dir = os.path.abspath(os.curdir)

    os.chdir(base)
    try:
        for path in paths:
            for dname, _unused_dirs, files in os.walk(path):
                for f in files:
                    file_list.add(os.path.join(dname, f))
    finally:
        os.chdir(cur_dir)

    return list(file_list)


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click',
]

setup(
    author="Jace Huang",
    author_email='jacehuang8@protonmail.ch',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English', 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    description="A self care bot.",
    entry_points={
        'console_scripts': [
            'perry-bot=perry_bot.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='perry_bot',
    name='perry_bot',
    packages=find_packages(include=['perry_bot', 'perry_bot.*']),
    package_data={
        module.__name__: walker(os.path.dirname(module.__file__), 'files'),
    },
    test_suite='tests',
    url='https://github.com/shunnkou/perry_bot',
    version='v0.1.0',
    zip_safe=False,
)
