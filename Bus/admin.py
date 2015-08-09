from django.contrib import admin
from Bus.models import BusStop, BusSchedule, BusRoute, BusProvider
# Register your models here.


admin.site.register(BusStop)
admin.site.register(BusSchedule)
admin.site.register(BusRoute)
admin.site.register(BusProvider)
