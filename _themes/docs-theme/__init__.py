"""
Large parts taken from the Guzzle Sphinx Theme
https://github.com/guzzle/guzzle_sphinx_theme/blob/master/guzzle_sphinx_theme/__init__.py
"""

import os


def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def setup(app):
    return {'parallel_read_safe': True}

def html_theme_path():
    return [os.path.dirname(os.path.abspath(__file__))]

