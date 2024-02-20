from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.EventAttendee)
admin.site.register(models.EventDetails)
admin.site.register(models.BatchClass)