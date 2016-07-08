#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'Arjun Biddanda'
SITEURL = u'http://localhost:8000'
SITENAME = u"Arjun Biddanda's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = u'Aspiring Mathematical Biologist'
SITELOGO = SITEURL + '/images/author.png'
FAVICON = SITEURL + '/images/author.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = u'index, follow'

THEME = u'/usr/local/lib/python3.5/site-packages/pelican/themes/Flex'
PATH = u'content'
TIMEZONE = u'America/Chicago'
DEFAULT_LANG = u'en'
OG_LOCALE = u'en_US'
LOCALE = u'en_US'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True

MAIN_MENU = True


SOCIAL = (('github', 'https://github.com/abiddanda'),
          ('twitter', 'https://twitter.com/aabiddanda'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

#CC_LICENSE = {
#    'name': 'Creative Commons Attribution-ShareAlike',
#    'version': '4.0',
#    'slug': 'by-sa'
# }

COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 5

PLUGINS = ['pelican_gist']

USE_LESS = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
