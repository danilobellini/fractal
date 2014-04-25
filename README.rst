..
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

#. Julia fractal

   ::

     python fractal.py julia -0.644 --size=300x200 --depth=25 --zoom=0.6 --show

   .. image:: images/julia_-0.644_size=300x200_depth=25_zoom=0.6.png

#. Julia fractal

   ::

     python fractal.py julia -0.7 +0.27015 j --size=500x300 --depth=512 --zoom=0.6 --show

   .. image:: images/julia_-0.7+0.27015j_size=500x300_depth=512_zoom=0.6.png

#. Julia fractal

   ::

     python fractal.py julia -0.7102 +0.2698 j --size=500x300 --depth=512 --zoom=0.65 --show

   .. image:: images/julia_-0.7102+0.2698j_size=500x300_depth=512_zoom=0.65.png

#. Julia fractal

   ::

     python fractal.py julia -0.8 +0.156 j --size=400x230 --depth=50 --zoom=0.65 --show

   .. image:: images/julia_-0.8+0.156j_size=400x230_depth=50_zoom=0.65.png

#. Julia fractal

   ::

     python fractal.py julia -0.8 +0.156 j --size=500x300 --depth=512 --zoom=0.6 --show

   .. image:: images/julia_-0.8+0.156j_size=500x300_depth=512_zoom=0.6.png

#. Julia fractal

   ::

     python fractal.py julia -1.037 +0.17 j --size=600x300 --depth=40 --zoom=0.55 --show

   .. image:: images/julia_-1.037+0.17j_size=600x300_depth=40_zoom=0.55.png

#. Mandelbrot fractal

   ::

     python fractal.py mandelbrot --size=300x300 --depth=80 --zoom=1.2 --center=-1x0 --show

   .. image:: images/mandelbrot_size=300x300_depth=80_zoom=1.2_center=-1x0.png

#. Mandelbrot fractal

   ::

     python fractal.py mandelbrot --size=400x300 --depth=80 --zoom=2 --center=-1x0 --show

   .. image:: images/mandelbrot_size=400x300_depth=80_zoom=2_center=-1x0.png

#. Mandelbrot fractal

   ::

     python fractal.py mandelbrot --size=500x500 --depth=256 --zoom=6.5 --center=-1.2x0.35 --show

   .. image:: images/mandelbrot_size=500x500_depth=256_zoom=6.5_center=-1.2x0.35.png

#. Mandelbrot fractal

   ::

     python fractal.py mandelbrot --size=500x500 --depth=80 --zoom=0.8 --center=-0.75x0 --show

   .. image:: images/mandelbrot_size=500x500_depth=80_zoom=0.8_center=-0.75x0.png

#. Mandelbrot fractal

   ::

     python fractal.py mandelbrot --size=600x600 --depth=256 --zoom=90 --center=-1.255x0.38 --show

   .. image:: images/mandelbrot_size=600x600_depth=256_zoom=90_center=-1.255x0.38.png


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