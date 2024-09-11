# Generated by Django 5.1 on 2024-09-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_membersession_team_alter_membersession_session"),
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
                ],
                max_length=6,
                unique=True,
            ),
        ),
    ]
