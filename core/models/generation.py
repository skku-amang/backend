from django.db import models


class Generation(models.Model):
    # 99.5기까지 허용
    order = models.DecimalField(max_digits=3, decimal_places=1, unique=True, verbose_name="기수")
    leader = models.ForeignKey(
        "user.CustomUser",
        null=True,
        on_delete=models.SET_NULL,
        related_name="leading_generations",
        verbose_name="기장",
    )

    def __str__(self) -> str:
        return f"{self.order}기"
    
    class Meta:
        ordering = ["order"]
        verbose_name = "기수"
        verbose_name_plural = "기수"
