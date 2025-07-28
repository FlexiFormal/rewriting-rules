import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))

project = 'rewriting-rules'
copyright = '2025, KWARC'
author = 'KWARC'

extensions = [
        'myst_parser',
        'sphinxextension',
]

myst_enable_extensions = [
        'dollarmath'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

def setup(app):
    app.add_css_file('rewriting.css')
