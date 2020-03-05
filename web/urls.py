#！/usr/bin/env python
#-*- coding:utf-8 -*-
from django.conf.urls import url
from web.views import *

urlpatterns = [
    #url(r'^index/',index,name="index"),
    url(r'^login/',login,name="login"),
]