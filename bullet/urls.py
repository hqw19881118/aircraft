# encoding:utf-8
from django.conf.urls import patterns, url
from bullet.views import *

urlpatterns = patterns('bullet.views',
                       url(r'^$', BulletListView.as_view(), name='bullet-list'),
                       url(r'^update/(?P<pk>\w+)/$', BulletUpdateView.as_view(), name='bullet-update'),
                       url(r'^delete/(?P<pk>\w+)/$', BulletDeleteView.as_view(), name='bullet-delete'),
                       url(r'^create/$', BulletCreateView.as_view(), name='bullet-create'),
                       )