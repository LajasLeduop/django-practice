from django.db import models
from datetime import datetime
now=datetime.now()

# Create your models here.
class EventDetails(models.Model):
    name = models.CharField(max_length=300)
    venue = models.CharField(max_length=200)
    venue_location = models.CharField(max_length=200)
    event_date=models.DateTimeField(default=now)
    event_details = models.TextField(default="Description of this event is not available")
    banner = models.ImageField(upload_to="images/")
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.name