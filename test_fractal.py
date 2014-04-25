#!/usr/bin/env py.test
# -*- coding: utf-8 -*-
# Created on Fri Apr 25 02:33:04 2014
# License is MIT, see COPYING.txt for more details.
# @author: Danilo de Jesus da Silva Bellini

import os, re, pytest
from fractal import generate_fractal, call_kw, cli_parse_args
from io import BytesIO
from pylab import imread, imsave


def show_parameters(fname):
  """ String with CLI args to show the fractal with the given ``fname`` """
  re_complex = re.compile("(?:([+-]?\s*[0-9.]+))?\s*"
                          "(?:([+-]\s*[0-9.]+)\s*)?(.*)")
  def part_generator():
    for part in fname.rsplit(".", 1)[0].split("_"):
      if "=" in part:
        yield "--" + part
      else:
        yield " ".join(filter(lambda x: x, re_complex.match(part).groups()))
    yield "--show"
  return " ".join(part_generator())


def to_dict_params(fname):
  """ Get full kwargs from file name """
  return cli_parse_args(show_parameters(fname).split())


@pytest.mark.parametrize("fname", os.listdir("images"))
def test_file_image(fname):
  ext = os.path.splitext(fname)[-1][len(os.path.extsep):]
  kwargs = to_dict_params(fname)

  # Creates the image in memory
  mem = BytesIO()
  fractal_data = call_kw(generate_fractal, kwargs)
  imsave(mem, fractal_data, cmap=kwargs["cmap"], format=ext)
  mem.seek(0) # Return stream position back for reading

  # Comparison pixel-by-pixel
  img_file = imread("images/" + fname)
  img_mem = imread(mem, format=ext)
  assert img_file.tolist() == img_mem.tolist()
