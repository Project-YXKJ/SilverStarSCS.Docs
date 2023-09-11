# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "SilverStar's CSSM Reference Book"
copyright = "2023, vayoger"
author = "vayoger"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_copybutton", "myst_parser", "sphinx_design"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "furo"
html_title = "SilverStar's CSSM Reference Book"
html_favicon = "_static/logo-square.svg"
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
# html_css_files = [
#     "css/custom.css",
# ]

html_theme_options = {
    # logo
    "light_logo": "logo-wide-light.svg",
    "dark_logo": "logo-wide-dark.svg",
    "light_css_variables": {
        # 衔接以及左侧目录的颜色
        "color-brand-primary": "#c0d725",
        "color-brand-content": "#c0d725",
    },
}
