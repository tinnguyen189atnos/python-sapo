#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup

setup(
    name="python-sapo",
    version="0.2",
    description="Python Sapo",
    author="NOS ERP Consulting (https://www.nostech.vn/)",
    author_email="odoo@nostech.vn",
    packages=["sapo"],
    install_requires=["requests"],
)
