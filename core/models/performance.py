from django.db import models


class Performance(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    representativeImage = models.ImageField(upload_to="performance/")
    location = models.CharField(max_length=255)
    startDatetime = models.DateTimeField()
    endDatetime = models.DateTimeField()
    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
