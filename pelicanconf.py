#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'anonrab'
SITENAME = u'anonrab@keep'
SITEURL = ''

PATH = 'content'
# путь к выходным html-файлам
# в целом настройка не важна,
# ибо генерировать всё, кроме постов
# будем в корень проекта
OUTPUT_PATH = 'articles/'
# как сохранять посты
ARTICLE_URL = 'articles/{slug}/'
# куда сохранять посты
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
