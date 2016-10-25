#!/usr/bin/env python
import os, setuptools, re

url = "https://github.com/danilobellini/fractal"

metadata = {
  "name": "fractal",
  "version": "0.1.0.dev",
  "author": "Danilo J. S. Bellini",
  "description": "Fractals in Python",
  "author_email": "danilo.bellini@gmail.com",
  "url": url,
  "license": "MIT",
  "py_modules": ["fractal"],
  "install_requires": ["matplotlib"],
}

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as f:
  metadata["long_description"] = re.sub(r"(\.\. (?:image|_\S+):+\s*)([^: ]+)",
                                        r"\1{0}/raw/master/\2".format(url),
                                        f.read())

metadata["classifiers"] = """
Development Status :: 3 - Alpha
License :: OSI Approved :: MIT License
Operating System :: POSIX :: Linux
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: Implementation :: CPython
Topic :: Artistic Software
Topic :: Multimedia :: Graphics
""".strip().splitlines()

setuptools.setup(**metadata)
