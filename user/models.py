from enum import Enum
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class Department(models.Model):
    CHOICES = [
        ("PERFORMANCE", "공연부"),
        ("PROMOTION", "홍보부"),
        ("PLANNING", "기획부"),
        ("INSTRUMENT", "악기부"),
    ]
    name = models.CharField(max_length=10)
    leader = models.ForeignKey(
        "CustomUser",
        null=True,
        on_delete=models.SET_NULL,
        related_name="leading_departments",
    )


class PositionChoices(Enum):
    PRESIDENT = "회장"
    VICE_PRESIDENT = "부회장"
    GENERAL_AFFAIRS = "총무"
    MEMBER = "일반"

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, nickname, password):
        if not email:
            raise ValueError("must have user email")
        user = self.model(email=self.normalize_email(email), nickname=nickname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email=self.normalize_email(email), nickname=nickname, password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    name = models.CharField(max_length=20)
    nickname = models.CharField(blank=True, max_length=20)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(blank=True)
    generation = models.ForeignKey("core.Generation", null=True, on_delete=models.PROTECT)
    session = models.ForeignKey("core.Session", null=True, on_delete=models.PROTECT)
    position = models.CharField(max_length=30, choices=PositionChoices.choices(), default=PositionChoices.MEMBER)
    department = models.ForeignKey(Department, null=True, on_delete=models.PROTECT)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    @property
    def is_amang_staff(self):
        if self.position == PositionChoices.MEMBER:
            return False
        return True
