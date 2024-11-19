from enum import Enum
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from core.models.generation import Generation


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
    회장 = "회장"
    부회장 = "부회장"
    총무 = "총무"
    일반 = "일반"

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(
        self,
        email: str,
        password: str,
        name: str,
        nickname: str,
        generation: int | Generation,
    ):
        if not email:
            raise ValueError("must have user email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.name = name
        user.nickname = nickname
        user.generation = generation
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        name: str,
        nickname: str,
        generation: int | Generation,
    ):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
            nickname=nickname,
            generation=generation,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="이메일",
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    name = models.CharField(max_length=20, blank=False, verbose_name="이름")
    nickname = models.CharField(
        max_length=20, unique=True, blank=False, verbose_name="닉네임"
    )
    bio = models.TextField(blank=True, verbose_name="소개")
    image = models.ImageField(blank=True, null=True, verbose_name="프로필 이미지")
    generation = models.ForeignKey(
        "core.Generation",
        null=True,
        on_delete=models.PROTECT,
        verbose_name="기수",
        related_name="users",
    )
    sessions = models.ManyToManyField(
        "core.Session", related_name="users", verbose_name="세션"
    )
    position = models.CharField(
        max_length=30,
        choices=PositionChoices.choices(),
        default=PositionChoices.일반,
        verbose_name="직책",
    )
    department = models.ForeignKey(
        Department, null=True, blank=True, on_delete=models.PROTECT, verbose_name="부서"
    )
    createdDatetime = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updatedDatetime = models.DateTimeField(auto_now=True, verbose_name="수정 일시")

    objects = UserManager()

    def __str__(self) -> str:
        generation = f"({self.generation})" if self.generation else ""
        return f"{self.name}{generation}"

    class Meta:
        ordering = ["generation__order", "name"]
        verbose_name = "유저"
        verbose_name_plural = "유저"
