# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for Latex
#       Use XeLaTex (to properly handle Unicode)
latex_engine = 'xelatex'

latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
     #
     # 'papersize': 'letterpaper',

     # The font size ('10pt', '11pt' or '12pt').
     #
     # 'pointsize': '10pt',
     #
     # Additional stuff for the LaTeX preamble.
     # (Currently, we don't do LaTeX -> PDF, because of issues with word order in Hebrew)
     #

     'preamble': r'''
\setmainfont{SBL_Hbrw.ttf}
\XeTeXlinebreaklocale "he"
\XeTeXlinebreakskip = 0pt plus 1pt
'''
}