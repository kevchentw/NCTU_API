from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def nctu_api_root(request, format=None):
    """
    NCTU API ROOT
    """
    return Response(
        {
            'bus': reverse('bus', request=request, format=format),
            'mail': reverse('mail-list', request=request, format=format),
        })

