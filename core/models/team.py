from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True)
    leader = models.ForeignKey("user.CustomUser", null=True, on_delete=models.SET_NULL)
    performance = models.ForeignKey("Performance", on_delete=models.PROTECT)
    isFreshmenFixed = models.BooleanField(default=False)
    posterImage = models.ImageField(upload_to="team_poster/", blank=True)

    # Song
    songName = models.CharField(max_length=50, blank=True)
    songArtist = models.CharField(max_length=50, blank=True)
    songYoutubeVideoId = models.CharField(max_length=50, blank=True)

    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}({self.leader})"


class MemberSession(models.Model):
    team = models.ForeignKey(
        "core.Team", on_delete=models.CASCADE, related_name="memberSessions"
    )
    session = models.ForeignKey("core.Session", on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(
        "user.CustomUser", related_name="registered_sessions"
    )
    requiredMemberCount = models.IntegerField()
