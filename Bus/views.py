from rest_framework import viewsets
from rest_framework import generics
from Bus.models import *
from Bus.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import filters


@api_view(('GET',))
def bus_root(request, format=None):
    return Response({
        'route': reverse('bus-route-list', request=request, format=format),
        'stop': reverse('bus-stop-list', request=request, format=format),
        'schedule': reverse('bus-schedule-list', request=request, format=format),
        'provider': reverse('bus-provider-list', request=request, format=format),
    })


# Bus Stop API
class BusStopList(generics.ListCreateAPIView):
    """
    Bus Stop API
    """
    queryset = BusStop.objects.all()
    serializer_class = BusStopSerializer


class BusStopDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Bus Stop API
    """
    queryset = BusStop.objects.all()
    serializer_class = BusStopSerializer



# Bus Schedule API
class BusScheduleList(generics.ListCreateAPIView):
    """
    Bus Schedule API
    """
    queryset = BusSchedule.objects.all()
    serializer_class = BusScheduleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('route',)


class BusScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Bus Schedule API
    """
    queryset = BusSchedule.objects.all()
    serializer_class = BusScheduleSerializer


# Bus Route API
class BusRouteList(generics.ListCreateAPIView):
    """
    Bus Route API
    """
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer


class BusRouteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Bus Route API
    """
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer


# Bus Provider API
class BusProviderList(generics.ListCreateAPIView):
    """
    Bus Provider API
    """
    queryset = BusProvider.objects.all()
    serializer_class = BusProviderSerializer


class BusProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Bus Provider API
    """
    queryset = BusProvider.objects.all()
    serializer_class = BusProviderSerializer