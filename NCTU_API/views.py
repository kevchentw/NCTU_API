from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def nctu_api_root(request, format=None):
    """
    ###NCTU OPEN API
    We are now under development...<br>
    If you are interested, please join our <a href="https://www.facebook.com/groups/331427716981279/"> Facebook Group</a>
    """
    return Response(
        {
            'bus': reverse('bus', request=request, format=format),
            'mail': reverse('mail-list', request=request, format=format),
            'building': reverse('building', request=request, format=format)
        })


