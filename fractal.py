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
depth = 256
width, height = 500, 300
cmap = "cubehelix" # Color map
model = "julia"
zoom = 1.7 # Ranges from [-zoom; +zoom] if center isn't changed
cx, cy = 0, 0 # Center point


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
fname_details = "_{cmap}_{width}x{height}_d={depth}_cp={cx}x{cy}_z={zoom}.png"
if model == "julia":
  func = lambda x, y: val(x, y, c)
  fname_template = "julia_c={c}" + fname_details
elif model == "mandelbrot":
  func = lambda x, y: val(0, 0, x + y * 1j)
  fname_template = "mandelbrot" + fname_details
else:
  raise ValueError("Fractal not found")

# Generates the intensities for each pixel
side = max(width, height)
deltax = (side - width) / 2 # Centralize
deltay = (side - height) / 2
img = pylab.array([
  [func(zoom * (2 * (col + deltax) / (side - 1) - 1) + cx,
        zoom * (2 * (height - row + deltay) / (side - 1) - 1) + cy)
    for col in range(width)]
  for row in range(height)
])

# Plots and saves the desired fractal raster image
pylab.imsave(fname_template.format(**locals()), img, cmap=cmap)
pylab.imshow(img, cmap=cmap)
pylab.show()
