from django.conf.urls import patterns, include, url
from rest_framework import routers
import Mail.views
from Bus.views import *
from NCTU_API.views import *

urlpatterns = patterns('',
                       url(r'^api/$', nctu_api_root),
                       url(r'^api/bus$', bus_root, name="bus"),
                       url(r'^api/bus/route/$', BusRouteList.as_view(), name='bus-route-list'),
                       url(r'^api/bus/route/(?P<pk>[0-9]+)/$', BusRouteDetail.as_view(), name='bus-route-detail'),
                       url(r'^api/bus/stop/$', BusStopList.as_view(), name='bus-stop-list'),
                       url(r'^api/bus/stop/(?P<pk>[0-9]+)/$', BusStopDetail.as_view(), name='bus-stop-detail'),
                       # url(r'^api/bus/stop/(?P<pk>[0-9]+)/highlight/$', BusStopHighlight.as_view(), name='bus-stop-highlight'),
                       url(r'^api/bus/schedule/$', BusScheduleList.as_view(), name='bus-schedule-list'),
                       url(r'^api/bus/schedule/(?P<pk>[0-9]+)/$', BusScheduleDetail.as_view(), name='bus-schedule-detail'),
                       url(r'^api/bus/provider/$', BusProviderList.as_view(), name='bus-provider-list'),
                       url(r'^api/bus/provider/(?P<pk>[0-9]+)/$', BusProviderDetail.as_view(), name='bus-provider-detail'),
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'mail', Mail.views.MailList.as_view()),
                       )
