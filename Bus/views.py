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
    ## Description

    > This method returns all the bus schedule, you can use filter to specify.

    ## GET Parameters
    ```
    GET /bus/schedule/?route=1&direction=True&weekend=True&format=json&type=string
    ```

    * Route
        * Parameter: `route`
        * Description: Get route by `Bus Route ID`
        * Notice: `Bus Route ID` can be found from `/bus/route/`
        * Value: `1` or other int

    * Direction
        * Parameter: `direction `
        * Description: Specify the direction of bus
        * Value
            * `True`: Outbound
            * `False`: Inbound

    * Semester
        * Parameter: `semester`
        * Description: Availability in semester days
        * Value
            * `True`: Yes
            * `False`: No

    * Vacation
        * Parameter: `vacation`
        * Description: Availability in vacation days
        * Value
            * `True`: Yes
            * `False`: No

    * Workday
        * Parameter: `semester`
        * Description: Availability in workday
        * Value
            * `True`: Yes
            * `False`: No

    * Weekend
        * Parameter: `weekend `
        * Description: Availability in weekend
        * Value
            * `True`: Yes
            * `False`: No

    * Format
        * Parameter: `format `
        * Description: Return format
        * Value
            * `api`: web interface
            * `json`: json

    * Type
        * Parameter: `type `
        * Description: Return type
        * Value
            * `id`: object as id
            * `string`: object as string

    **Notice**

    - `bollean` parameters should be `True` or `False`

    ## Sources

    - http://www.ga.nctu.edu.tw/ga2/files/business/20140917101302.html
    - http://www.hcbus.com.tw/big5/information-2.asp?select=2
    """
    def get_serializer_class(self):
        if 'type' in self.request.query_params:
            if self.request.query_params['type'] == 'string':
                return BusScheduleSerializerString
            if self.request.query_params['type'] == 'id':
                return BusScheduleSerializer
        return BusScheduleSerializer
    queryset = BusSchedule.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('route', 'direction', 'semester', 'vacation', 'workday', 'weekend')


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
