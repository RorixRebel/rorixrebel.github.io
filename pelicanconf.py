#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'Miguel Valdes'
SITENAME = 'Dev-Mex'
SITESUBTITLE = 'IT mexicaning'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# MD
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'}
    },
    'output_format': 'html5',
}

# THEME
THEME = 'personal'
THEME_STATIC_DIR = 'static'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'styles.css'

# MISC
DEFAULT_PAGINATION = 5
TYPOGRIFY = True
