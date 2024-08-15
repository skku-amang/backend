from django.db import models


class Performance(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()