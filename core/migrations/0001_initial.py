# Generated by Django 5.1 on 2024-11-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True)),
                ("createdDatetime", models.DateTimeField(auto_now_add=True)),
                ("updatedDatetime", models.DateTimeField(auto_now=True)),
                ("startDatetime", models.DateTimeField()),
                ("endDatetime", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="FeedbackAnswer",
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
                ("answer", models.TextField()),
                ("createdDatetime", models.DateTimeField(auto_now_add=True)),
                ("updatedDatetime", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="FeedbackQuestion",
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
                ("question", models.TextField()),
                (
                    "questionType",
                    models.CharField(
                        choices=[("string", "String"), ("int", "Integer")],
                        default="string",
                        max_length=50,
                    ),
                ),
                ("order", models.IntegerField()),
                ("isRequired", models.BooleanField(default=True)),
            ],
        ),
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
                (
                    "order",
                    models.DecimalField(decimal_places=1, max_digits=3, unique=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MemberSession",
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
            ],
        ),
        migrations.CreateModel(
            name="MemberSessionMembership",
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
                ("index", models.IntegerField()),
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
                ("description", models.TextField(blank=True, null=True)),
                (
                    "representativeImage",
                    models.ImageField(null=True, upload_to="performance/"),
                ),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("startDatetime", models.DateTimeField(blank=True, null=True)),
                ("endDatetime", models.DateTimeField(blank=True, null=True)),
                ("createdDatetime", models.DateTimeField(auto_now_add=True)),
                ("updatedDatetime", models.DateTimeField(auto_now=True)),
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
                ("icon", models.ImageField(null=True, upload_to="session/")),
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
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("description", models.TextField(blank=True)),
                ("isFreshmenFixed", models.BooleanField(default=False)),
                ("isSelfMade", models.BooleanField(default=False)),
                (
                    "posterImage",
                    models.ImageField(blank=True, upload_to="team_poster/"),
                ),
                ("songName", models.CharField(blank=True, max_length=50)),
                ("songArtist", models.CharField(blank=True, max_length=50)),
                ("songYoutubeVideoId", models.CharField(blank=True, max_length=50)),
                ("createdDatetime", models.DateTimeField(auto_now_add=True)),
                ("updatedDatetime", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
