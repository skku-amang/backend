# Generated by Django 5.1 on 2024-09-10 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_rename_created_datetime_team_createddatetime_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="song",
            old_name="cover_artist",
            new_name="coverArtist",
        ),
        migrations.RenameField(
            model_name="song",
            old_name="cover_name",
            new_name="coverName",
        ),
        migrations.RenameField(
            model_name="song",
            old_name="cover_url",
            new_name="coverUrl",
        ),
        migrations.RenameField(
            model_name="song",
            old_name="original_url",
            new_name="originalUrl",
        ),
    ]
