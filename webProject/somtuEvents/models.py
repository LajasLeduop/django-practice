from django.db import models
from datetime import datetime,timedelta
import os
now=datetime.now()
end_date=now+timedelta(hours=1)

# Create your models here.
class EventDetails(models.Model):
    name = models.CharField(max_length=300)
    venue = models.CharField(max_length=200)
    venue_location = models.CharField(max_length=200)
    event_start_date=models.DateTimeField(default=now)
    event_end_date=models.DateTimeField(default=end_date)
    event_details = models.TextField(default="Description of this event is not available")
    banner = models.ImageField(upload_to="images/")
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
    # Delete the associated image file before deleting the event object
        if self.banner:
            # Get the path to the image file
            image_path = self.banner.path
            # Check if the file exists before attempting to delete it
            if os.path.exists(image_path):
                # Delete the file
                os.remove(image_path)
        # Call the superclass delete method to delete the event object
        super().delete(*args, **kwargs)
    
class EventAttendee(models.Model):
    
    attendee_name=models.CharField(max_length=200)
    attendee_email=models.EmailField(max_length=100)
    attendee_phone=models.CharField(max_length=20)
    attendee_class=models.CharField(max_length=30)
    is_somtu_student=models.BooleanField(default=False)
    event=models.ForeignKey(EventDetails, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.attendee_name
    
class BatchClass(models.Model):
    class_name=models.CharField(max_length=30)
    class_stream=models.CharField(max_length=20)
    class_batch=models.IntegerField()

    def __str__(self):
        return self.class_name + " " + self.class_stream + " " + str(self.class_batch)