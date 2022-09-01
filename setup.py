#!/usr/bin/env python

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name="superpro",
     version="0.4.5",
     # version=version,
     scripts=[],
     author="Stefan Volk",
     author_email="pliable.bride_0o@icloud.com",
     description="tools",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/f17mkx/superpip",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )


