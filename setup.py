#!/usr/bin/env python3

from setuptools import setup, find_packages
import os

with open("README.md", "r") as readme:
    long_description = readme.read()


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name="7seg-ByteBird",
    version="0.2",
    author="samedamci",
    author_email="samedamci@disroot.org",
    description=(
        'Simple "Flappy Bird" like game for 7 segment display from ZeroSeg module for Raspberry Pi.'
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samedamci/7seg-ByteBird",
    project_urls={"Issue tracker": "https://github.com/samedamci/7seg-ByteBird/issues"},
    packages=find_packages(),
    license="ISC",
    keywords="raspberry pi rpi led seven segment zeroseg game",
    python_requires=">=3.6",
    install_requires=read("requirements.txt").splitlines(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: POSIX :: Linux",
    ],
    entry_points={
        'console_scripts': [
            'bytebird = ByteBird.game:main',
        ],
    },
)
