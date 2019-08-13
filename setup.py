#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
#   Author(s): Milan Falesnik   <milan@falesnik.net>
#                               <mfalesni@redhat.com>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from setuptools import setup


setup(
    name="kwargify",
    use_scm_version=True,
    author="Milan Falešník",
    author_email="milan@falesnik.net",
    description="Python function kwargifier",
    license="GPLv2",
    keywords="kwargs",
    url="https://github.com/mfalesni/python-kwargify",
    py_modules=["kwargify"],
    setup_requires = ['setuptools', 'setuptools_scm', 'wheel'],
    install_requires=[],
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ]
)
