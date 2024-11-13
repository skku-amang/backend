from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="이름")
    description = models.TextField(blank=True, verbose_name="설명")
    leader = models.ForeignKey("user.CustomUser", null=True, on_delete=models.SET_NULL, verbose_name="팀장")
    performance = models.ForeignKey("Performance", on_delete=models.CASCADE, verbose_name="공연")
    isFreshmenFixed = models.BooleanField(default=False, verbose_name="신입 고정 여부")
    isSelfMade = models.BooleanField(default=False, verbose_name="자작곡 여부")
    posterImage = models.ImageField(upload_to="team_poster/", blank=True, null=True, verbose_name="포스터 이미지")

    # Song
    songName = models.CharField(max_length=50, blank=True, verbose_name="곡 명")
    songArtist = models.CharField(max_length=50, blank=True, verbose_name="아티스트")
    songYoutubeVideoId = models.CharField(max_length=50, blank=True, verbose_name="유튜브 비디오 ID")

    createdDatetime = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updatedDatetime = models.DateTimeField(auto_now=True, verbose_name="수정 일시")

    def __str__(self) -> str:
        return f"[{self.performance}] {self.name}(곡: {self.songName}, 팀장: {self.leader})"
    
    class Meta:
        ordering = ["performance", "-createdDatetime"]
        verbose_name = "팀"
        verbose_name_plural = "팀"


class MemberSession(models.Model):
    team = models.ForeignKey(
        "core.Team", on_delete=models.CASCADE, related_name="memberSessions",
        verbose_name="팀"
    )
    session = models.ForeignKey("core.Session", on_delete=models.SET_NULL, null=True, verbose_name="세션")

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
        MemberSession, on_delete=models.CASCADE, related_name="members", verbose_name="팀 구성 세션"
    )
    member = models.ForeignKey(
        "user.CustomUser", on_delete=models.CASCADE, null=True, blank=True, verbose_name="멤버"
    )
    index = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.memberSession}{self.index} - {self.member}"
    
    class Meta:
        ordering = ["memberSession", "index"]
        verbose_name = "팀 세션별 멤버"
        verbose_name_plural = "팀 세션별 멤버"
