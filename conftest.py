"""Py.test configuration module/"plugin"."""
import sys, itertools


def count(start=0, step=1):
    """A ``itertools.count`` with a ``step`` parameter on Python 2.6."""
    while True:
        yield start
        start += step


def pytest_configure(config):
    """Py.test hook to replace ``itertools.count`` on Python 2.6."""
    if sys.version_info < (2,7):
        itertools.count = count
