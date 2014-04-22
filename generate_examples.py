#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on Tue Apr 22 07:14:05 2014
# @author: Danilo de Jesus da Silva Bellini

from fractal import Point, exec_command
from collections import OrderedDict

# String formatting functions
Point.__str__ = lambda self: "x".join(map(str, self))
basic_str = lambda el: str(el).lstrip("(").rstrip(")") # Complex or model name
item_str = lambda k, v: (basic_str(v) if k in ["model", "c"] else
                         "{}={}".format(k, v))
filename = lambda kwargs: "_".join(item_str(*pair) for pair in kwargs.items())

# Example list
kwargs_list = [
  OrderedDict([("model", "julia"),
               ("c", -.7102+.2698j),
               ("size", Point(500, 300)),
               ("depth", 512),
               ("zoom", .65),
  ]),
  OrderedDict([("model", "julia"),
               ("c", -1.037+.17j),
               ("size", Point(600, 300)),
               ("depth", 40),
               ("zoom", .55),
  ]),
  OrderedDict([("model", "julia"),
               ("c", -.644),
               ("size", Point(300, 200)),
               ("depth", 25),
               ("zoom", .6),
  ]),
  OrderedDict([("model", "julia"),
               ("c", -.7+.27015j),
               ("size", Point(500, 300)),
               ("depth", 512),
               ("zoom", .6),
  ]),
  OrderedDict([("model", "julia"),
               ("c", -.8+.156j),
               ("size", Point(500, 300)),
               ("depth", 512),
               ("zoom", .6),
  ]),
  OrderedDict([("model", "julia"),
               ("c", -.8+.156j),
               ("size", Point(400, 230)),
               ("depth", 50),
               ("zoom", .65),
  ]),
  OrderedDict([("model", "mandelbrot"),
               ("size", Point(500, 500)),
               ("depth", 80),
               ("zoom", .8),
               ("center", Point(-.75, 0)),
  ]),
  OrderedDict([("model", "mandelbrot"),
               ("size", Point(300, 300)),
               ("depth", 80),
               ("zoom", 1.2),
               ("center", Point(-1, 0)),
  ]),
  OrderedDict([("model", "mandelbrot"),
               ("size", Point(400, 300)),
               ("depth", 80),
               ("zoom", 2),
               ("center", Point(-1, 0)),
  ]),
  OrderedDict([("model", "mandelbrot"),
               ("size", Point(500, 500)),
               ("depth", 256),
               ("zoom", 6.5),
               ("center", Point(-1.2, .35)),
  ]),
  OrderedDict([("model", "mandelbrot"),
               ("size", Point(600, 600)),
               ("depth", 256),
               ("zoom", 90),
               ("center", Point(-1.255, .38)),
  ]),
]

# Creates all examples
for kwargs in kwargs_list:
  kwargs["output"] = "images/{}.png".format(filename(kwargs))
  #kwargs["show"] = True
  exec_command(kwargs)
