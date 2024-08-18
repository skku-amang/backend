# Generated by Django 5.1 on 2024-08-18 09:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='generation',
            name='leader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leading_generations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='session',
            name='세션장',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leading_sessions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='song',
            name='satisfied_sessions',
            field=models.ManyToManyField(related_name='songs_satisfying', to='core.session'),
        ),
        migrations.AddField(
            model_name='song',
            name='unsatisfied_sessions',
            field=models.ManyToManyField(related_name='songs_unsatisfying', to='core.session'),
        ),
        migrations.AddField(
            model_name='team',
            name='leader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='performance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.performance'),
        ),
        migrations.AddField(
            model_name='song',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.team'),
        ),
    ]
