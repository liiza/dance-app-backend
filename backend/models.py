from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

class Dance(models.Model):
    name = models.CharField(max_length=255, null=True)

class DanceRecord(models.Model):
    dance = models.ForeignKey('Dance')
    # Speed m/s per direction
    x_speed = models.FloatField()
    y_speed = models.FloatField()
    z_speed = models.FloatField()
    # The of the position as nanoseconds
    time = models.IntegerField()

