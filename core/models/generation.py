from django.db import models


class Generation(models.Model):
    order = models.IntegerField()
    leader = models.ForeignKey('user.CustomUser', null=True, on_delete=models.SET_NULL)
