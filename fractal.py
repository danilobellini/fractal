#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on Tue Apr 08 08:45:59 2014
# @author: Danilo de Jesus da Silva Bellini
"""
Julia and Mandelbrot fractals image creation
"""

from __future__ import division
import pylab, argparse, collections, inspect

Point = collections.namedtuple("Point", ["x", "y"])

def pair_reader(dtype):
  return lambda data: Point(*map(dtype, data.lower().split("x")))


DEFAULT_SIZE = "512x512"
DEFAULT_DEPTH = "256"
DEFAULT_ZOOM = "1"
DEFAULT_CENTER = "0x0"
DEFAULT_COLORMAP = "cubehelix"


def generate_fractal(model, c=None, size=pair_reader(int)(DEFAULT_SIZE),
                     depth=int(DEFAULT_DEPTH), zoom=float(DEFAULT_ZOOM),
                     center=pair_reader(float)(DEFAULT_CENTER)):
  """ Returns a 2D Numpy Array with the fractal value for each pixel """
  width, height = size
  cx, cy = center

  # Algorithm
  def val(x, y, c):
    """
    Gaston Julia Fractal value for pixel at coords [x, y].
    """
    result = 0
    number = x + y * 1j
    while result < depth and number.real ** 2 + number.imag ** 2 < 4:
      number = number ** 2 + c
      result += 1
    return result

  # Selects the model
  if model == "julia":
    func = lambda x, y: val(x, y, c)
  elif model == "mandelbrot":
    func = lambda x, y: val(0, 0, x + y * 1j)
  else:
    raise ValueError("Fractal not found")

  # Generates the intensities for each pixel
  side = max(width, height)
  deltax = (side - width) / 2 # Centralize
  deltay = (side - height) / 2
  img = pylab.array([
    [func((2 * (col + deltax) / (side - 1) - 1) / zoom + cx,
          (2 * (height - row + deltay) / (side - 1) - 1) / zoom + cy)
      for col in range(width)]
    for row in range(height)
  ])

  return img


def img2output(img, cmap=DEFAULT_COLORMAP, output=None, show=False):
  """ Plots and saves the desired fractal raster image """
  if output:
    pylab.imsave(output, img, cmap=cmap)
  if show:
    pylab.imshow(img, cmap=cmap)
    pylab.show()


def exec_command(kwargs):
  """ Fractal command from a dictionary of keyword arguments (from CLI) """
  keys_gf = inspect.getargspec(generate_fractal).args
  kwargs_gf = {k: v for k, v in kwargs.items() if k in keys_gf}
  img = generate_fractal(**kwargs_gf)
  keys_i2o = inspect.getargspec(img2output).args
  kwargs_i2o = {k: v for k, v in kwargs.items() if k in keys_i2o}
  img2output(img, **kwargs_i2o)


if __name__ == "__main__":
  # CLI interface description
  parser = argparse.ArgumentParser(
    description=__doc__,
    epilog="by Danilo J. S. Bellini",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
  )
  parser.add_argument("model", choices=["julia", "mandelbrot"],
                      help="Fractal type/model")
  parser.add_argument("c", nargs="*", default=argparse.SUPPRESS,
                      help="Single Julia fractal complex-valued constant "
                           "parameter (needed for julia, shouldn't appear "
                           "for mandelbrot), e.g. -.7102 + .2698j (with the "
                           "spaces), or perhaps with zeros and 'i' like "
                           "-0.6 + 0.4i. If the argument parser gives "
                           "any trouble, just add spaces between the numbers "
                           "and their signals, like '- 0.6 + 0.4 j'")
  parser.add_argument("-s", "--size", default=DEFAULT_SIZE,
                      type=pair_reader(int),
                      help="Size in pixels for the output file")
  parser.add_argument("-d", "--depth", default=DEFAULT_DEPTH,
                      type=int,
                      help="Iteration depth, the step count limit")
  parser.add_argument("-z", "--zoom", default=DEFAULT_ZOOM,
                      type=float,
                      help="Zoom factor, assuming data is shown in the "
                           "[-1/zoom; 1/zoom] range for both dimensions, "
                           "besides the central point displacement")
  parser.add_argument("-c", "--center", default=DEFAULT_CENTER,
                      type=pair_reader(float),
                      help="Central point in the image")
  parser.add_argument("-m", "--cmap", default=DEFAULT_COLORMAP,
                      help="Matplotlib colormap name to be used")
  parser.add_argument("-o", "--output", default=argparse.SUPPRESS,
                      help="Output to a file, with the chosen extension, "
                           "e.g. fractal.png")
  parser.add_argument("--show", default=argparse.SUPPRESS,
                      action="store_true",
                      help="Shows the plot in the default Matplotlib backend")

  # Process arguments
  args = parser.parse_args()
  if args.model == "julia" and "c" not in args:
    parser.error("Missing Julia constant")
  if args.model == "mandelbrot" and "c" in args:
    parser.error("Mandelbrot has no constant")
  if "output" not in args and "show" not in args:
    parser.error("Nothing to be done (no output file name nor --show)")
  if "c" in args:
    try:
      args.c = complex("".join(args.c).replace("i", "j"))
    except ValueError as exc:
      parser.error(exc)

  # Execute the given command
  exec_command(vars(args))
