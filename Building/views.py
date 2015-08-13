from rest_framework import viewsets
from rest_framework import generics
from Building.models import *
from Building.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import filters


@api_view(('GET',))
def building_root(request, format=None):
    return Response({
        'building': reverse('building-list', request=request, format=format),
        'campus': reverse('campus-list', request=request, format=format),
        })

class CampusList(generics.ListCreateAPIView):
    """
    Campus API
    """
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class CampusDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Campus API
    """
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class BuildingList(generics.ListCreateAPIView):
    """
    Building API
    """
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Building API
    """
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
