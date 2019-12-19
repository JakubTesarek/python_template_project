# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------
project = '<project_name>'
copyright = '<author_name>'
author = '<author_name>'
release = '1.0.0'
extensions = ['sphinxcontrib.spelling', 'sphinx.ext.autodoc']
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
master_doc = 'index'
spelling_word_list_filename = ['spelling.txt']
