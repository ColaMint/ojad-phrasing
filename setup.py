#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='ojad-phrasing',
    version='0.1',
    url='https://github.com/Everley1993/ojad-phrasing',
    description='oajd phrasing',
    license='MIT',
    author='Everley',
    author_email='463785757@qq.com',
    platforms=['any'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ojad-phrasing=ojad_phrasing.main:main',
        ],
    },
    install_requires=[
	'certifi==2017.11.5',
	'chardet==3.0.4',
	'cssselect==1.0.3',
	'idna==2.6',
	'lxml==4.1.1',
	'requests==2.18.4',
	'urllib3==1.24.2',
    ],
    include_package_data=True,
)
