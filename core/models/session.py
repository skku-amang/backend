from django.db import models


class Session(models.Model):
    name = models.CharField(
        choices=[
            ("VOCAL", "보컬"),
            ("GUITAR", "기타"),
            ("BASS", "베이스"),
            ("SYNTH", "신디"),
            ("DRUM", "드럼"),
        ],
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

    def __str__(self) -> str:
        return self.name
