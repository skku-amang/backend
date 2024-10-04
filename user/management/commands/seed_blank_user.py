import uuid
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create a blank user with id = 0 if not exists"

    def handle(self, *args, **kwargs):
        try:
            User = get_user_model()
            email = User.BLANK_USER_EMAIL
            random_password = str(uuid.uuid4())
            random_nickname = self.generate_unique_random_nickname()

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
        except Exception as e:
            self.style.ERROR(
                f"Error while creating blank user with {User.BLANK_USER_EMAIL}"
            )
            raise e

    @classmethod
    def generate_unique_random_nickname(cls):
        User = get_user_model()
        random_nickname = str(uuid.uuid4())
        user_with_random_nickname = User.objects.filter(nickname=random_nickname)

        if user_with_random_nickname.count() == 0:
            return random_nickname
        return cls.generate_unique_random_nickname()
