#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on Sun Apr 20 00:37:12 2014
# License is MIT, see COPYING.txt for more details.
# @author: Danilo de Jesus da Silva Bellini

from __future__ import unicode_literals
import os, io
from test_fractal import show_parameters

template_string = """..
  README.rst created with generate_readme.py, don't edit this file manually.
  License is MIT, see COPYING.txt for more details.

Fractals in Python
==================

Repository with Python code that renders fractals, compatible with both Python
2.7 and 3.2+, showing and saving files with Matplotlib.

For more information about the maths used for fractals (as well as its
history), see the Wikipedia pages about the
`Julia set`_ and `Mandelbrot set`_.

.. _`Julia set`: https://en.wikipedia.org/wiki/Julia_set
.. _`Mandelbrot set`: https://en.wikipedia.org/wiki/Mandelbrot_set


Examples
--------
{% for fname in sorted(listdir("images")) %}
#. {{fname.split("_")[0].capitalize()}} fractal

   ::

     python fractal.py {{show_parameters(fname)}}

   .. image:: images/{{fname}}
{% endfor %}

Parameters
----------

Examples above can also be done with a ``--output fractal.png`` parameter,
which saves the example to a image file, while ``--show`` just shows the
raster fractal image on the screen (both parameters can be used together).
For more help, see::

  python fractal.py --help

Which shows all options available. To see all colormaps names available in
Matplotlib, see the `colormaps on the scipy wiki`_ or type in a Python shell:

.. code-block:: python

  [m for m in __import__("pylab").cm.datad if not m.endswith("_r")]

.. _`colormaps on the scipy wiki`:
   http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps

----

License is MIT, see `COPYING.txt`_ for more details.
By Danilo J. S. Bellini

.. _`COPYING.txt`: COPYING.txt
"""

kwargs = {
  "listdir": os.listdir,
  "sorted": sorted,
  "show_parameters": show_parameters,
}

if __name__ == "__main__":
  import jinja2
  template = jinja2.Template(template_string)
  readme_data = template.render(**kwargs)

  with io.open("README.rst", "w", encoding="utf-8", newline="\r\n") as readme:
    readme.write(readme_data)
