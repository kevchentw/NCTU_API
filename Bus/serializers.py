from rest_framework import serializers
from Bus.models import BusStop, BusSchedule, BusRoute, BusProvider
import django_filters

class BusStopSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='bus-stop-detail')

    class Meta:
        model = BusStop
        fields = ('id', 'name_ZH', 'name_EN', 'description_ZH', 'description_EN', 'lat', 'lon', 'url')


class BusStopForScheduleSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='bus-provider-detail')

    class Meta:
        model = BusStop
        fields = ('name_ZH', 'name_EN', 'url')


class BusProviderForRouteSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='bus-provider-detail')

    class Meta:
        model = BusProvider
        fields = ('name_ZH', 'name_EN', 'url')


class BusRouteForScheduleSerializer(serializers.ModelSerializer):
    provider = BusProviderForRouteSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='bus-route-detail')

    class Meta:
        model = BusRoute
        fields = ('name_ZH',
                  'name_EN',
                  'provider',
                  'url'
                  )


class BusScheduleSerializer(serializers.ModelSerializer):
    # route = serializers.StringRelatedField()
    # stop = serializers.HyperlinkedIdentityField(view_name='bus-provider-detail')
    url = serializers.HyperlinkedIdentityField(view_name='bus-schedule-detail')

    class Meta:
        model = BusSchedule
        fields = ('id', 'time', 'route', 'stop', 'direction', 'description_ZH', 'description_EN', 'url')


class BusProviderSerializer(serializers.ModelSerializer):
    route_provider = serializers.StringRelatedField(many=True)

    class Meta:
        model = BusProvider
        fields = ('id', 'name_ZH', 'name_EN', 'route_provider')


class BusRouteSerializer(serializers.ModelSerializer):
    provider = BusProviderForRouteSerializer(read_only=True)
    departure = BusStopSerializer(read_only=True)
    destination = BusStopSerializer(read_only=True)

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



