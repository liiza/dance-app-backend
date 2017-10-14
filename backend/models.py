from django.db import models


class Record(models.Model):
    json_data = models.CharField(max_length=1024) 
