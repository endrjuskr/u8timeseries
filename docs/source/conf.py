# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
#
# One should be careful here. If there is a version of the package installed somewhere
# on the computer when building the documentation, it has priority. Therefore changes
# to the "local" source code might not be reflected on the documentation.

# Fix of issue above: use pip install -e <package directory> to install the module.

import os
import sys

# To set the abspath below, we assume that the tree of the directory is as follows:
#
# u8timeseries
# docs
#  |___ source
#          |____ conf.py
#
sys.path.insert(0, os.path.abspath('../../'))


# -- Project information -----------------------------------------------------

project = 'u8timeseries'
copyright = '2019, unit8'
author = 'unit8'

# The full version, including alpha/beta/rc tags
release = 'v0.0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# TODO: Fix sphinx_rtd_theme (add in requirements.txt? yes a priori)
# For now: use default html theme.

html_theme = 'default'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['/docs/html/_static']
