from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=40)
    nickname = models.CharField(max_length=40)
    bio = models.TextField()
    profile_image = models.ImageField()
    # generation = models.ForeignKey('core.Generation', on_delete=models.PROTECT)
    # session = models.ForeignKey('core.Session', on_delete=models.PROTECT)
