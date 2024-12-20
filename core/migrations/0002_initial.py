# Generated by Django 5.1 on 2024-11-12 06:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="feedbackanswer",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="feedbackquestion",
            name="feedback",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="core.feedback",
            ),
        ),
        migrations.AddField(
            model_name="feedbackanswer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="core.feedbackquestion",
            ),
        ),
        migrations.AddField(
            model_name="generation",
            name="leader",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="leading_generations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="membersessionmembership",
            name="member",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="membersessionmembership",
            name="memberSession",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="members",
                to="core.membersession",
            ),
        ),
        migrations.AddField(
            model_name="feedback",
            name="performance",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="feedbacks",
                to="core.performance",
            ),
        ),
        migrations.AddField(
            model_name="session",
            name="세션장",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="leading_sessions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="membersession",
            name="session",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.session",
            ),
        ),
        migrations.AddField(
            model_name="team",
            name="leader",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="team",
            name="performance",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.performance"
            ),
        ),
        migrations.AddField(
            model_name="membersession",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="memberSessions",
                to="core.team",
            ),
        ),
        migrations.AddConstraint(
            model_name="membersession",
            constraint=models.UniqueConstraint(
                fields=("team", "session"), name="unique_team_session"
            ),
        ),
    ]
