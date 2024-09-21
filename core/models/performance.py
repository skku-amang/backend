from django.db import models


class Performance(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    representativeImage = models.ImageField(upload_to="performance/", null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    startDatetime = models.DateTimeField(blank=True, null=True)
    endDatetime = models.DateTimeField(blank=True, null=True)

    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
