from django.conf.urls import patterns, include, url
from rest_framework import routers
import Mail.views
from Bus.views import BusStopViewSet, BusScheduleViewSet, BusRouteViewSet, BusProviderViewSet
router = routers.DefaultRouter()
router.register(r'bus_stop', BusStopViewSet)
router.register(r'bus_schedule', BusScheduleViewSet)
router.register(r'bus_route', BusRouteViewSet)
router.register(r'bus_provider', BusProviderViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'mail', Mail.views.MailList.as_view())
                       )
