from Mail.models import Mail
from rest_framework import serializers


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ('name', 'date', 'mail_id', 'mail_type', 'dorm')

