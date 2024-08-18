from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)
    leader = models.ForeignKey('user.CustomUser', null=True, on_delete=models.SET_NULL)
    performance = models.ForeignKey('Performance', on_delete=models.PROTECT)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}({self.leader})"


class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    cover_name = models.CharField(max_length=255, blank=True)
    cover_artist = models.CharField(max_length=255, blank=True)
    original_url = models.URLField(blank=True)
    cover_url = models.URLField(blank=True)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    satisfied_sessions = models.ManyToManyField('Session', related_name="songs_satisfying")
    unsatisfied_sessions = models.ManyToManyField('Session', related_name="songs_unsatisfying")

    def __str__(self) -> str:
        return f"{self.name}({self.artist})"
