import os
import sys

sys.path.insert(0, os.path.abspath("../"))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "package_name"
copyright = "2025, <owner_name>"
author = "<owner_name>"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",  # Enables Markdown support
    "sphinx.ext.autodoc",  # Automatically generates documentation from docstrings
    "sphinx.ext.napoleon",  # Supports NumPy and Google-style docstrings
    "sphinx.ext.autosummary",  # Generates summary tables for modules and classes
    "sphinx_autodoc_typehints",  # Adds type hints from Python annotations
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for autodoc -----------------------------------------------------

autodoc_default_options = {
    "members": True,  # Document class members
    "undoc-members": True,  # Include undocumented members
    "private-members": True,  # Include private members (_ prefixed)
    "special-members": "__call__, __repr__, __eq__, __len__, __iter__, __contains__",  # Include special methods like __init__
    "inherited-members": True,  # Include inherited members
    "show-inheritance": True,  # Show class inheritance
}

napoleon_google_docstring = True  # Enable Google-style docstrings
napoleon_numpy_docstring = True  # Enable NumPy-style docstrings

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
