# Generated by Django 5.1 on 2024-10-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_alter_performance_enddatetime_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="generation",
            name="order",
            field=models.DecimalField(decimal_places=1, max_digits=3, unique=True),
        ),
    ]
