from enum import Enum
from django.db import models


class Department(models.Model):
    CHOICES = [
        ("PERFORMANCE", "공연부"),
        ("PROMOTION", "홍보부"),
        ("PLANNING", "기획부"),
        ("INSTRUMENT", "악기부")
    ]
    name = models.CharField(max_length=10)
    leader = models.ForeignKey('CustomUser', null=True, on_delete=models.SET_NULL, related_name="leading_departments")


class PositionChoices(Enum):
    PRESIDENT = "회장"
    VICE_PRESIDENT = "부회장"
    GENERAL_AFFAIRS = "총무"
    MEMBER = "일반"

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class CustomUser(models.Model):
    name = models.CharField(max_length=40)
    nickname = models.CharField(max_length=40)
    bio = models.TextField()
    profile_image = models.ImageField()
    generation = models.ForeignKey('core.Generation', on_delete=models.PROTECT)
    session = models.ForeignKey('core.Session', on_delete=models.PROTECT)
    position = models.CharField(max_length=30, choices=PositionChoices.choices())
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    @property
    def is_amang_staff(self):
        if self.position == PositionChoices.MEMBER:
            return False
        return True
