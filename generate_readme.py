#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on Sun Apr 20 00:37:12 2014
# @author: Danilo de Jesus da Silva Bellini

from __future__ import unicode_literals
import os, re, jinja2, io

template_string = """..
  README.rst created with generate_readme.py, don't edit this file manually.

Fractals in Python
==================

Repository with Python code that renders fractals, compatible with both Python
2.7 and 3.2+.

For more information about the maths used for fractals (as well as its
history), see the Wikipedia pages about the
`Julia set`_ and `Mandelbrot set`_.

.. _`Julia set`: https://en.wikipedia.org/wiki/Julia_set
.. _`Mandelbrot set`: https://en.wikipedia.org/wiki/Mandelbrot_set


Examples
--------
{% for fname in sorted(listdir("images"))
%}{% with width, height, depth, c = re_julia.match(fname).groups() %}
Julia Fractal for constant ``{{c}}`` and depth ``{{depth}}``, with
{{width}}x{{height}} pixels

.. image:: images/{{fname}}
{% endwith %}{% endfor %}
"""

template_globals = {
  "listdir": os.listdir,
  "sorted": sorted,
  "re_julia": re.compile("julia_(.*?)x(.*?)_d=(.*?)_c=\(?(.*?)\)?.png"),
}

env = jinja2.Environment(extensions=["jinja2.ext.with_"])
template = env.from_string(template_string, globals=template_globals)

with io.open("README.rst", "w", encoding="utf-8", newline="\r\n") as readme:
  readme.write(template.render())
