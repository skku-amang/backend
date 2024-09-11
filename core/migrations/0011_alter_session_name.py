# Generated by Django 5.1 on 2024-09-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_alter_session_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="session",
            name="name",
            field=models.CharField(
                choices=[
                    ("보컬", "보컬"),
                    ("기타", "기타"),
                    ("베이스", "베이스"),
                    ("신디", "신디"),
                    ("드럼", "드럼"),
                    ("현악기", "현악기"),
                    ("관악기", "관악기"),
                ],
                max_length=6,
                unique=True,
            ),
        ),
    ]
