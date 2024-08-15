from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_private = models.BooleanField()
    leader = models.ForeignKey('user.CustomUser', null=True, on_delete=models.SET_NULL)
    performance = models.ForeignKey('Performance', on_delete=models.PROTECT)


class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    cover_name = models.CharField(max_length=255)
    cover_artist = models.CharField(max_length=255)
    original_url = models.URLField()
    cover_url = models.URLField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    satisfied_sessions = models.ManyToManyField('Session', related_name="songs_satisfying")
    unsatisfied_sessions = models.ManyToManyField('Session', related_name="songs_unsatisfying")
