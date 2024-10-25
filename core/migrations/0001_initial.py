# Generated by Django 5.1 on 2024-08-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Generation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Performance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("start_datetime", models.DateTimeField()),
                ("end_datetime", models.DateTimeField()),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("updated_datetime", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("VOCAL", "보컬"),
                            ("GUITAR", "기타"),
                            ("BASS", "베이스"),
                            ("SYNTH", "신디"),
                            ("DRUM", "드럼"),
                        ],
                        max_length=6,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("artist", models.CharField(max_length=255)),
                ("cover_name", models.CharField(blank=True, max_length=255)),
                ("cover_artist", models.CharField(blank=True, max_length=255)),
                ("original_url", models.URLField(blank=True)),
                ("cover_url", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True)),
                ("is_private", models.BooleanField(default=False)),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("updated_datetime", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
