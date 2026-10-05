# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import tibas.tt
import alabaster
import os
import sys

sys.path.append(os.path.abspath("_ext"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Home Recipes"
copyright = "2026, SeekingAura"
author = "SeekingAura"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_design",
    # Local custom
    "card_simple",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "tt"
html_theme_path = [tibas.tt.get_path(), alabaster.get_path()]
html_static_path = ["_static"]
html_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.3.1/js/all.js",
]

html_permalinks_icon = ""


html_show_copyright = False
# theme_extra_nav_links = False
html_show_sphinx = False
html_theme_show_powered_by = False
html_show_source = False
logo_url = ""
