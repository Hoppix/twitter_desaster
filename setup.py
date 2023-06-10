#!/usr/bin/env python3

import setuptools

install_requires = [
        ]

setuptools.setup(
    name="touchme",
    python_requires=">=3.8",
    description="Predicting real desasters from tweets",
    version="0.1",
    author="Kolja Hopfmann",
    author_email="k.hopfmann@hotmail.de",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    )
