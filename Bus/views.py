from Bus.models import BusStop, BusSchedule, BusProvider, BusRoute
from rest_framework import viewsets
from Bus.serializers import BusStopSerializer, BusScheduleSerializer, BusRouteSerializer, BusProviderSerializer
from rest_framework import generics
from rest_framework import filters


class BusStopViewSet(viewsets.ModelViewSet):
    """
    Bus Stop API
    """
    queryset = BusStop.objects.all()
    serializer_class = BusStopSerializer


class BusScheduleViewSet(viewsets.ModelViewSet):
    """
    Bus Schedule API
    """
    queryset = BusSchedule.objects.all()
    serializer_class = BusScheduleSerializer


class BusRouteViewSet(viewsets.ModelViewSet):
    """
    Bus Route API
    """
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer


class BusProviderViewSet(viewsets.ModelViewSet):
    """
    Bus Provider API
    """
    queryset = BusProvider.objects.all()
    serializer_class = BusProviderSerializer
