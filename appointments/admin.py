from django.contrib import admin

from appointments.models import Appointment, VaccineSchedule

# Register your models here.
admin.site.register(Appointment)
admin.site.register(VaccineSchedule)