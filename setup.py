from setuptools import setup, find_packages
from os import path

setup(
    name="pssg",
    version="0.0.94",
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=["markdown",],
    scripts=['./bin/pssg'],
)
