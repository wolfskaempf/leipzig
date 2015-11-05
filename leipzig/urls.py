"""leipzigcore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^programme/$', programme, name='programme'),
    url(r'^updates/$', updates, name='updates'),
    url(r'^articles/$', articles, name='articles'),
    url(r'^article/(?P<pk>[0-9]+)/$', article_single, name='article_single'),
    url(r'^wish/$', song_wish, name='song_wish'),
    url(r'^partners/$', partners, name='partners'),
    url(r'^dictionary/$', dictionary, name='dictionary'),
    url(r'^phones/$', phones, name='phones'),
    url(r'^houses/$', houses, name='houses'),
    url(r'^topics/$', topics, name='topics'),
    url(r'^topic/(?P<pk>[0-9]+)/$', topic_single, name='topic_single'),
    url(r'^feedback/$', feedback, name='feedback'),
    url(r'^imprint/$', imprint, name='imprint'),
    url(r'^datenschutzerklaerung/$', datenschutzerklaerung, name='datenschutzerklaerung'),
]
