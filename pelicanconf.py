#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Julian Wergieluk'
SITENAME = 'Julian Wergieluk'

PATH = 'content'
THEME = 'themes/custom'
#PLUGIN_PATHS = ['/home/julian/clones/pelican-plugins',]
#PLUGINS = ['i18n_subsites', ]
#JINJA_ENVIRONMENT = {'extensions': 'jinja2.ext.i18n'}

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'

DATE_FORMATS = {
    'en': '%m/%d/%Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/jwergieluk'),
          ('LinkedIn', 'http://www.linkedin.com/pub/julian-wergieluk'),)

GOOGLE_ANALYTICS = 'UA-26503219-1'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'static/robots.txt',
    ]
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    }

