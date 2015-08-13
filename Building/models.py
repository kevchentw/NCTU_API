from django.db import models

class Building(models.Model):
    name_ZH = models.CharField(max_length=50)
    name_EN = models.CharField(max_length=50)
    classroom_code = models.CharField(max_length=5)
    campus = models.ForeignKey('Campus', related_name='building_campus')
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s (%s)" %(self.name_ZH, self.name_EN)

class Campus(models.Model):
    name_ZH = models.CharField(max_length=50)
    name_EN = models.CharField(max_length=50)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s (%s)" %(self.name_ZH, self.name_EN)


