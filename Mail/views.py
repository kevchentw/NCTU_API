from Mail.models import Mail
from rest_framework import viewsets
from Mail.serializers import MailSerializer
import django_filters
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MailFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name="name__name")
    permission_classes = (IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Mail
        fields = ('name', 'date', 'mail_id', 'mail_type', 'dorm')


class MailList(generics.ListAPIView):
    """
    Mail API
    """
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    filter_class = MailFilter
    search_fields = ('name',)
    ordering_fields = ('date',)
    ordering = ('-date',)
