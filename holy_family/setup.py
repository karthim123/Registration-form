# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in holy_family/__init__.py
from holy_family import __version__ as version

setup(
	name='holy_family',
	version=version,
	description='Holy_Family_Hospital ',
	author='Kartik Mangla',
	author_email='kam1941028@sicsr.ac.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
