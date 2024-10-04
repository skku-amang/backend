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
        "user.CustomUser",
        related_name="registered_sessions",
        through="MemberSessionMembership",
    )


class MemberSessionMembership(models.Model):
    # MemberSession과 CustomUser 사이의 m2m 관계를 정의하는 모델입니다.
    # 장고의 m2m 필드는 두 모델 모두를 pk로 설정하기 때문에
    # 한 인스턴스를 동일한 키의 다른 여러 개의 인스턴스가 참조할 수 없게 됩니다.
    # 따라서 이러한 중복을 허용하기 위해 이 모델을 따로 정의합니다.
    # 중복을 허용하는 이유는 공백 유저가 여러번 등록되는 경우가 있기 때문입니다.
    # 다만, 로컬(SQLite)에서는 deferrable unique constraints가 적용되지 않기에 중복이 불가능합니다.
    member_session = models.ForeignKey(MemberSession, on_delete=models.CASCADE)
    custom_user = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["member_session", "custom_user"],
                name="unique_member_session_custom_user",
                deferrable=models.Deferrable.DEFERRED,
            )
        ]
