from django.db import models


class Session(models.Model):
    NAME_CHOICES = ["보컬", "기타", "베이스", "신디", "드럼", "현악기", "관악기"]
    name = models.CharField(
        choices=[(name, name) for name in NAME_CHOICES],
        max_length=6,
        unique=True,
    )
    leader = models.ForeignKey(
        "user.CustomUser",
        name="세션장",
        null=True,
        on_delete=models.SET_NULL,
        related_name="leading_sessions",
    )
    icon = models.ImageField(upload_to="session/", null=True)

    def __str__(self) -> str:
        return self.name
