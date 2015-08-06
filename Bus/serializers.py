from rest_framework import serializers
from Bus.models import BusStop, BusSchedule, BusRoute, BusProvider


class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStop
        fields = ('id', 'name_ZH', 'name_EN', 'description_ZH', 'description_EN', 'lat', 'lon')


class BusScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSchedule
        fields = ('id', 'time', 'route', 'stop', 'description_ZH', 'description_EN', 'lat', 'lon')


class BusRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusRoute
        fields = ('id', 'name_ZH', 'name_EN', 'provider', 'departure', 'destination', 'description_ZH', 'description_EN')


class BusProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusProvider
        fields = ('id', 'name_ZH', 'name_EN')
