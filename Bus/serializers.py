from rest_framework import serializers
from Bus.models import BusStop, BusSchedule, BusRoute, BusProvider
import django_filters


class BusStopSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='bus-stop-detail')

    class Meta:
        model = BusStop
        fields = ('id',
                  'name_ZH',
                  'name_EN',
                  'description_ZH',
                  'description_EN',
                  'lat',
                  'lon',
                  'url')



class BusScheduleSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='bus-schedule-detail')
    class Meta:
        model = BusSchedule
        fields = ('id',
                  'time',
                  'route',
                  'stop',
                  'direction',
                  'description_ZH',
                  'description_EN',
                  'semester',
                  'vacation',
                  'workday',
                  'weekend',
                  'url')


class BusScheduleSerializerString(serializers.ModelSerializer):
    route = serializers.StringRelatedField()
    stop = serializers.StringRelatedField()
    url = serializers.HyperlinkedIdentityField(view_name='bus-schedule-detail')
    class Meta:
        model = BusSchedule
        fields = ('id',
                  'time',
                  'route',
                  'stop',
                  'direction',
                  'description_ZH',
                  'description_EN',
                  'semester',
                  'vacation',
                  'workday',
                  'weekend',
                  'url')

class BusProviderSerializer(serializers.ModelSerializer):
    route_provider = serializers.StringRelatedField(many=True)

    class Meta:
        model = BusProvider
        fields = ('id',
                  'name_ZH',
                  'name_EN',
                  'route_provider')


class BusRouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusRoute
        fields = ('id',
                  'name_ZH',
                  'name_EN',
                  'provider',
                  'departure',
                  'destination',
                  'description_ZH',
                  'description_EN',
                  )



