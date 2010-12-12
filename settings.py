#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Contributors:
#   Pos Brolet 		
#   	You       
#   	You       
#
# Copyright 2010 pykhmer.org
# All rights reserved
#
import os.path
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
# Django settings for pykhmerWEB project.
gettext = lambda s: s #translate message
DEBUG = True
TEMPLATE_DEBUG = DEBUG
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'site_media') # Store media files such as image ...
#MEDIA_URL = '/media/'
#Ensure that you have set your own MEDIA_URL variable to something other than 'Media' as this conflicts with the default CMS Admin media Url. There's a note at the bottom of the documentation about this. 
MEDIA_URL = '/site_media/'
ADMINS = (
    # ('pos brolet', 'admin@pykhmer.org'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',			 # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pykhmer.db',            # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': 'localhost',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

ADMIN_MEDIA_PREFIX = '/media/admin/'
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ae53yv%tdwpg-50wlzz=0#%!fu=5klzs&+4p%lq_-(b*&t%zpn'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware', 
    'django.middleware.locale.LocaleMiddleware',  
    'cms.middleware.page.CurrentPageMiddleware', 
    'cms.middleware.user.CurrentUserMiddleware', 
	 "cms.middleware.media.PlaceholderMediaMiddleware",
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

#TEMPLATE_DIRS = os.path.join(PROJECT_PATH, 'templates')

CMS_TEMPLATES = (
        ('base.html', gettext('default')),
        ('2col.html', gettext('2 Column')),
        ('3col.html', gettext('3 Column')),
        ('extra.html', gettext('Some extra fancy template')),
)
LANGUAGES = (
        ('km', gettext('Khmer')),#Khmer language is priority
        ('en', gettext('English')),
)
LANGUAGE_CODE = 'km'
ROOT_URLCONF = 'pykhmerWEB.urls'
CMS_TEMPLATE_INHERITANCE = True
#Template will be us for pykhmer.org webiste .currently I am using 2col.html inheritance from base.html
CMS_TEMPLATES = ( 
    ('base.html', gettext('default')), 
    ('2col.html', gettext('2 Column')), 
    ('3col.html', gettext('3 Column')), 
    ('extra.html', gettext('Some extra fancy template')),
) 

MS_PLACEHOLDER_CONF = {
        'content': {
                'plugins': ('TextPlugin', 'PicturePlugin'),
                'extra_context': {"theme":"wide"},
                'name':gettext("Content")
		},
		'right-column': {
				"plugins": ('TeaserPlugin', 'LinkPlugin'),
				"extra_context": {"theme":"small"},
                'name':gettext("Right Column")
		},
}


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth', 
    'django.core.context_processors.i18n', 
    'django.core.context_processors.request', 
    'django.core.context_processors.media', 
    'cms.context_processors.media',
)
#CMS_USE_TINYMCE = True
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
	'cms',
	#'tinymce', #TODO Next
	'south',			#Database migration when we need workig with database we need to comment this line
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'mptt',
	'tagging',
	#'zinnia.plugins',# the blog plugin #TODO Next
	'menus',
    'publisher',	
	'django.contrib.admin',
	'django.contrib.sites',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)
