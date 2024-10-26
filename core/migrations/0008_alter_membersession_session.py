# Generated by Django 5.1 on 2024-09-10 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_team_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membersession",
            name="session",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="memberSessions",
                to="core.session",
            ),
        ),
    ]
