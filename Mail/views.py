from Mail.models import Mail
from rest_framework import viewsets
from Mail.serializers import MailSerializer
import django_filters
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MailList(generics.ListCreateAPIView):
    """
    ## Description

    > This method returns all the student mail, you can use filter to specify.

    ## Update

    Data will update every 5 minutes.

    ## GET Parameters
    ```
    GET /mail/?search=陳&dorm=十舍&mail_type=平信&format=json
    ```

    * Search
        * Parameter: `search`
        * Description: Search mail by name
        * Value: Any string
    * Dorm
        * Parameter: `dorm`
        * Description: Select from specific dorm
        * Value
            * `九舍`
            * `十舍`
            * ...
    * Mail Type
        * Parameter: `mail_type`
        * Description: Availability in vacation days
        * Value
            * `普掛`
            * `平信`
            * ...
    * Format
        * Parameter: `format `
        * Description: Return format
        * Value
            * `api`: web interface
            * `json`: json


    ## Sources
    - http://mailsys.nctu.edu.tw/MailNotify/

    """
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)
    filter_fields = ('dorm','mail_type', )


class MailDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Mail API
    """
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
