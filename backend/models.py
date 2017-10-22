from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

class Record(models.Model):
    json_data = JSONField(max_length=1024) 

class DanceRecord(models.Model):
    dance = models.ForeignKey('Dance')
    # Speed m/s per direction
    x_speed = models.FloatField()
    y_speed = models.FloatField()
    z_speed = models.FloatField()
    # The of the position as nanoseconds
    time = models.IntegerField()
    
class Dance(models.Model):
    name = models.CharField(max_length=255, null=True)
