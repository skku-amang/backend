# Generated by Django 5.1 on 2024-10-04 11:19

import django.db.models.constraints
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_merge_20241004_2017"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="membersessionmembership",
            constraint=models.UniqueConstraint(
                deferrable=django.db.models.constraints.Deferrable["DEFERRED"],
                fields=("member_session", "custom_user"),
                name="unique_member_session_custom_user",
            ),
        ),
    ]
