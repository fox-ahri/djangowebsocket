
#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
import sys
import os
from setuptools import setup, find_packages

path = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(path, 'README.md')) as f:
        long_description = f.read()
except Exception as e:
    long_description = "django websocket"

setup(
    name="djangowebsocket",
    version="1.0.1",
    author="ahri",
    author_email="ahriknow@gmail.com",
    description="pip python django3 websocket",
    keywords=("pip", "python", "django", "websocket"),
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.5.0",
    license = "MIT Licence",
    url="https://github.com/fox-ahri/djangowebsocket",
    packages=['djangowebsocket'],
    platforms = "any",
    install_requires=[],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)