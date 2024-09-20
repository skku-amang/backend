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

    def __str__(self) -> str:
        return self.name


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

    def create_user(self, email, password):
        if not email:
            raise ValueError("must have user email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
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
    profileImage = models.ImageField(blank=True)
    generation = models.ForeignKey(
        "core.Generation", null=True, on_delete=models.PROTECT
    )
    sessions = models.ManyToManyField("core.Session", related_name="users")
    position = models.CharField(
        max_length=30,
        choices=PositionChoices.choices(),
        default=PositionChoices.MEMBER,
    )
    department = models.ForeignKey(Department, null=True, on_delete=models.PROTECT)
    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        generation = f"({self.generation})" if self.generation else ""
        return f"{self.name}{generation}"
