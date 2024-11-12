from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True)
    leader = models.ForeignKey("user.CustomUser", null=True, on_delete=models.SET_NULL)
    performance = models.ForeignKey("Performance", on_delete=models.CASCADE)
    isFreshmenFixed = models.BooleanField(default=False)
    isSelfMade = models.BooleanField(default=False)
    posterImage = models.ImageField(upload_to="team_poster/", blank=True)

    # Song
    songName = models.CharField(max_length=50, blank=True)
    songArtist = models.CharField(max_length=50, blank=True)
    songYoutubeVideoId = models.CharField(max_length=50, blank=True)

    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}({self.leader})"
    
    class Meta:
        ordering = ["-createdDatetime"]
        verbose_name = "팀"
        verbose_name_plural = "팀"


class MemberSession(models.Model):
    team = models.ForeignKey(
        "core.Team", on_delete=models.CASCADE, related_name="memberSessions"
    )
    session = models.ForeignKey("core.Session", on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.team} - {self.session}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["team", "session"], name="unique_team_session"
            )
        ]
        ordering = ["team", "session"]
        verbose_name = "팀 세션"
        verbose_name_plural = "팀 세션"


class MemberSessionMembership(models.Model):
    memberSession = models.ForeignKey(
        MemberSession, on_delete=models.CASCADE, related_name="members"
    )
    member = models.ForeignKey(
        "user.CustomUser", on_delete=models.CASCADE, null=True, blank=True
    )
    index = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.memberSession} - {self.member}({self.index})"
    
    class Meta:
        ordering = ["memberSession", "index"]
        verbose_name = "팀 세션별 멤버"
        verbose_name_plural = "팀 세션별 멤버"
