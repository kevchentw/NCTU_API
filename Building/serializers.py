from rest_framework import serializers
import django_filters
from Building.models import Building, Campus

class BuildingSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='building-detail')
    campus = serializers.StringRelatedField()

    class Meta:
        model = Building
        fields = ('id',
                'name_ZH',
                'name_EN',
                'campus',
                'lat',
                'lon',
                'url',)


class CampusSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='campus-detail')

    class Meta:
        model = Campus
        fields = ('id',
                'name_ZH',
                'name_EN',
                'lat',
                'lon',
                'url',)
