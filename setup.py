#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright:
#   2019 P. H. <github.com/perfide>
# License:
#   BSD-2-Clause (BSD 2-Clause "Simplified" License)
#   https://spdx.org/licenses/BSD-2-Clause.html

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='px-ldap-replace',
    version='0.0.1',
    scripts=['px-ldap-replace'],
    author='P. H.',
    author_email='px-ldap-replace.perfide@safersignup.de',
    description='A LDAP regex replace script',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/perfide/px-ldap-replace',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
)
