from django.conf.urls import patterns, include, url
from rest_framework import routers
import Mail.views

router = routers.DefaultRouter()





urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'mail', Mail.views.MailList.as_view())
)
