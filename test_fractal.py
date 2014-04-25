#!/usr/bin/env py.test
# -*- coding: utf-8 -*-
# Created on Fri Apr 25 02:33:04 2014
# License is MIT, see COPYING.txt for more details.
# @author: Danilo de Jesus da Silva Bellini

import os, re, pytest, pylab
from fractal import generate_fractal, call_kw, cli_parse_args, img2output
from io import BytesIO
from pylab import imread, imsave, array
p = pytest.mark.parametrize

#
# Helper functions
#

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


def almost_equal_diff(a, b, max_diff = 2e-2):
  return abs(a - b) < max_diff


#
# Tests!
#

@p("fname", os.listdir("images"))
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


def test_generate_fractal_wrong_name(): # Only possible from API
  with pytest.raises(ValueError):
    generate_fractal(model="julia_")


class TestImg2Output(object):
  """ Tests interface with Matplotlib """

  def test_file_as_memory_output(self):
    img = array([[0, 1], [1, 0], [.5, .3]])
    mem = BytesIO()
    img2output(img, cmap="gray", output=mem)
    mem.seek(0)
    png_data = imread(mem)
    for row_png, row_img in zip(png_data, img):
      for pixel_png, pixel_img in zip(row_png, row_img):
        assert almost_equal_diff(pixel_png[-1], 1.)
        for pixel in pixel_png[:-1]:
          assert almost_equal_diff(pixel, pixel_img)

  def test_show(self, monkeypatch):
    def imshow(img, cmap):
      assert not imshow.called
      assert cmap == "gray"
      assert img.shape == (3, 2)
      imshow.called = True
    def show():
      assert imshow.called
    monkeypatch.setattr(pylab, "imshow", imshow)
    monkeypatch.setattr(pylab, "show", show)

    img = array([[0, 1], [1, 0], [.5, .3]])
    imshow.called = False
    assert img2output(img, cmap="gray", show=True) is None

  def test_show_and_output(self, monkeypatch):
    def imsave(output, img, cmap): # Should be called first
      assert not imsave.called
      assert not imshow.called
      assert cmap == "something"
      assert img.shape == (2, 4)
      imsave.called = True
      output.write(b"Data!")
    def imshow(img, cmap):
      assert imsave.called
      assert not imshow.called
      assert cmap == "something"
      assert img.shape == (2, 4)
      imshow.called = True
    def show():
      assert imsave.called
      assert imshow.called
    monkeypatch.setattr(pylab, "imsave", imsave)
    monkeypatch.setattr(pylab, "imshow", imshow)
    monkeypatch.setattr(pylab, "show", show)

    img = array([[5, -1, 4, .0003], [.1, 0., 47.8, -8]])
    imshow.called = False
    imsave.called = False
    mem = BytesIO()
    assert img2output(img, cmap="something", output=mem, show=True) is None
    mem.seek(0)
    assert mem.read() == b"Data!"
