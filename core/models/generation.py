from django.db import models


class Generation(models.Model):
    order = models.IntegerField()
    leader = models.ForeignKey('user.CustomUser', null=True, on_delete=models.SET_NULL, related_name="leading_generations")

    def __str__(self) -> str:
        return f"{self.order}기"
