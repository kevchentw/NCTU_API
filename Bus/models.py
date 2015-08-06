from django.db import models


class BusStop(models.Model):
    name_ZH = models.CharField(max_length=50)
    name_EN = models.CharField(max_length=50)
    description_ZH = models.TextField(default="")
    description_EN = models.TextField(default="")
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s(%s)" % (self.name_ZH, self.name_EN)


class BusRoute(models.Model):
    name_ZH = models.CharField(max_length=50)
    name_EN = models.CharField(max_length=50)
    departure = models.ForeignKey('BusStop', related_name='route_departure')
    destination = models.ForeignKey('BusStop', related_name='route_destination')
    provider = models.ForeignKey('BusProvider', related_name='route_provider')
    description_ZH = models.TextField(default="")
    description_EN = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s(%s)" % (self.name_ZH, self.name_EN)


class BusSchedule(models.Model):
    time = models.TimeField()
    route = models.ForeignKey('BusRoute', related_name='schedule_route')
    stop = models.ForeignKey('BusStop', related_name='schedule_stop')
    description_ZH = models.TextField(default="")
    description_EN = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s(%s)" % (self.time, self.route, self.stop)


class BusProvider(models.Model):
    name_ZH = models.CharField(max_length=50)
    name_EN = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s(%s)" % (self.name_ZH, self.name_EN)
