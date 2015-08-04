from django.db import models


class BusStop(models.Model):
    name_ZH = models.CharField(max_length=50)
    name_EN = models.CharField(max_length=50)
    description_ZH = models.TextField()
    description_EN = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BusRoute(models.Model):
    name_ZH = models.CharField(max_length=50)
    name_EN = models.CharField(max_length=50)
    departure = models.ForeignKey('BusStop',related_name='person_book')
    destination = models.ForeignKey('BusStop')
    provider = models.CharField(max_length=50)
    description_ZH = models.TextField()
    description_EN = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BusSchedule(models.Model):
    time = models.TimeField()
    route = models.ForeignKey('BusRoute')
    stop = models.ForeignKey('BusStop')
    description_ZH = models.TextField()
    description_EN = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
