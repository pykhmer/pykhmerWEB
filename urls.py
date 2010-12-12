#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Contributors:
#   Pos Brolet -- 2010
#   	       -- 2010
#
# Copyright 2010 pykhmer.org
# All rights reserved
#
from django.conf.urls.defaults import *
from django.contrib import admin
import os.path
admin.autodiscover()
site_media = os.path.join(os.path.dirname(__file__), 'site_media')
urlpatterns = patterns('', 
    
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': site_media }),	
    (r'^admin/', include(admin.site.urls)),
	#(r'^admin/(.*)', admin.site.root),
    (r'^', include('cms.urls')),
)