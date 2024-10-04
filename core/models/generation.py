from django.db import models


class Generation(models.Model):
    # 99.5기까지 허용
    order = models.DecimalField(max_digits=3, decimal_places=1, unique=True)
    leader = models.ForeignKey(
        "user.CustomUser",
        null=True,
        on_delete=models.SET_NULL,
        related_name="leading_generations",
    )

    def __str__(self) -> str:
        return f"{self.order}기"
