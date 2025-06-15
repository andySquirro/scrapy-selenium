"""
Packaging script for scrapy-selenium (patched for modern pip)
"""

from pathlib import Path
from setuptools import setup, find_packages


def get_requirements(path):
    """
    Read a requirements file, returning a list with comments / empty
    lines stripped.
    """
    lines = (l.strip() for l in Path(path).read_text().splitlines())
    return [l for l in lines if l and not l.startswith("#")]


setup(
    name="scrapy-selenium",
    version="0.0.0+local",        # or read it from a file / tag
    description="Scrapy middleware that drives a Selenium browser",
    author="Original authors",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=get_requirements("requirements/requirements.txt"),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)