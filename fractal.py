#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on Tue Apr 08 08:45:59 2014
# @author: Danilo de Jesus da Silva Bellini
"""
Gaston Julia fractal (1917)
"""

from __future__ import division
import pylab

# Parameters
c = -.7102 + .2698j
depth = 512
width, height = 512, 512
cmap = "cubehelix" # Color map
model = "mandelbrot"

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
  fname_template = "julia_{cmap}_{width}x{height}_d={depth}_c={c}.png"
elif model == "mandelbrot":
  func = lambda x, y: val(0, 0, x + y * 1j)
  fname_template = "mandelbrot_{cmap}_{width}x{height}_d={depth}.png"
else:
  raise ValueError("Fractal not found")

# Generates the intensities for each pixel mapped to the (-2; 2) range
side = max(width, height)
img = pylab.array([
  [func(2 * col / (width - 1) - 1, 2 * row / (height - 1) - 1)
    for col in range(width)]
  for row in range(height)
])

# Plots and saves the desired fractal raster image
pylab.imsave(fname_template.format(**locals()), img, cmap=cmap)
pylab.imshow(img, cmap=cmap)
pylab.show()
