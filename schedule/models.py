from django.db import models
from event.models import Event
from speaker.models import Speaker
# Create your models here.


class Schedule(models.Model):
     event = models.ForeignKey(Event, on_delete=models.CASCADE)
     start_time = models.TimeField(null=True, blank=True)
     end_time = models.TimeField(null=True, blank=True)
     topic = models.CharField(max_length=200)
     speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE, blank=True, null=True)

     class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
        ordering = ["id"]
  

     def __str__(self):
        return self.topic