# -*- coding: utf-8 -*-
#Created on Tue Apr  8 08:45:59 2014
#@author: danilo
"""
Gaston Julia fractal (1917)
"""

from __future__ import division
import pylab

#c = -.7 + .27015j
c = -.7102 + .2698j
#c = -1.037 + .17j
#c = -.8 +.156

def val(x, y, m=512):
  result = 0
  while x ** 2 + y ** 2 < 4 and result < m:
    number = (x + y * 1j) ** 2 + c
    x, y = number.real, number.imag
    result += 1
  return result

width, height = 512, 512
side = max(width, height)

img = pylab.array([
  [val(2 * col / (width - 1) - 1, 2 * row / (height - 1) - 1)
    for col in range(width)]
  for row in range(height)
])

pylab.imsave("julia_fractal_{}.png".format(c), img, cmap="cubehelix")
pylab.imshow(img, cmap="cubehelix")
pylab.show()
