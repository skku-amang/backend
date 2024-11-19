# Generated by Django 5.1 on 2024-11-13 13:04

import django.db.models.deletion
import user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_alter_generation_leader_alter_generation_order_and_more"),
        ("user", "0002_alter_customuser_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="bio",
            field=models.TextField(blank=True, verbose_name="소개"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="createdDatetime",
            field=models.DateTimeField(auto_now_add=True, verbose_name="생성 일시"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="user.department",
                verbose_name="부서",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=255, unique=True, verbose_name="이메일"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="generation",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="core.generation",
                verbose_name="기수",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="프로필 이미지"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="name",
            field=models.CharField(max_length=20, verbose_name="이름"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="nickname",
            field=models.CharField(max_length=20, unique=True, verbose_name="닉네임"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="position",
            field=models.CharField(
                choices=[
                    ("회장", "회장"),
                    ("부회장", "부회장"),
                    ("총무", "총무"),
                    ("일반", "일반"),
                ],
                default=user.models.PositionChoices["일반"],
                max_length=30,
                verbose_name="직책",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="sessions",
            field=models.ManyToManyField(
                related_name="users", to="core.session", verbose_name="세션"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="updatedDatetime",
            field=models.DateTimeField(auto_now=True, verbose_name="수정 일시"),
        ),
    ]