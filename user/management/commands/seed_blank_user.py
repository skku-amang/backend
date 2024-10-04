import uuid
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create a blank user with id = 0 if not exists"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = User.BLANK_USER_EMAIL
        random_password = str(uuid.uuid4())
        random_nickname = User.BLANK_USER_NICKNAME

        if not User.objects.filter(email=email).exists():
            User.objects.create(
                email=email, password=random_password, nickname=random_nickname
            )
            self.stdout.write(
                self.style.SUCCESS(f"Blank User {email} created successfully.")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Blank User with email {email} already exists.")
            )
