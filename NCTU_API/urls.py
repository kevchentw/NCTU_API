from django.conf.urls import patterns, include, url
from rest_framework import routers
import Mail.views
from Bus.views import *
from NCTU_API.views import *
from django.contrib import admin

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
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'mail', Mail.views.MailList.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       )
