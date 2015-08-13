from django.conf.urls import patterns, include, url
from rest_framework import routers
from Mail.views import *
from Bus.views import *
from Building.views import *
from NCTU_API.views import *
from django.contrib import admin
from rest_framework.authtoken import views

urlpatterns = patterns('',
                       url(r'^$', nctu_api_root),
                       url(r'^bus$', bus_root, name="bus"),
                       url(r'^bus/route/$', BusRouteList.as_view(), name='bus-route-list'),
                       url(r'^bus/route/(?P<pk>[0-9]+)/$', BusRouteDetail.as_view(), name='bus-route-detail'),
                       url(r'^bus/stop/$', BusStopList.as_view(), name='bus-stop-list'),
                       url(r'^bus/stop/(?P<pk>[0-9]+)/$', BusStopDetail.as_view(), name='bus-stop-detail'),
                       url(r'^bus/schedule/$', BusScheduleList.as_view(), name='bus-schedule-list'),
                       url(r'^bus/schedule/(?P<pk>[0-9]+)/$', BusScheduleDetail.as_view(), name='bus-schedule-detail'),
                       url(r'^bus/provider/$', BusProviderList.as_view(), name='bus-provider-list'),
                       url(r'^bus/provider/(?P<pk>[0-9]+)/$', BusProviderDetail.as_view(), name='bus-provider-detail'),
                       url(r'^mail/$', MailList.as_view(), name='mail-list'),
                       url(r'^mail/(?P<pk>[0-9]+)/$', MailDetail.as_view(), name='mail-detail'),
                       url(r'^building$', building_root, name="building"),
                       url(r'^building/building/$', BuildingList.as_view(), name='building-list'),
                       url(r'^building/building/(?P<pk>[0-9]+)/$', BuildingDetail.as_view(), name='building-detail'),
                       url(r'^building/campus/$', CampusList.as_view(), name='campus-list'),
                       url(r'^building/campus/(?P<pk>[0-9]+)/$', CampusDetail.as_view(), name='campus-detail'),
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-token-auth/', views.obtain_auth_token),
                       )
