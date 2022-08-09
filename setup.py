#!/usr/bin/env python

import setuptools
# import sys
#
# version= sys.argv[2]

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='superpro',
     version='0.3',
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

if __name__ == "__main__":
    print(setuptools.find_packages())
