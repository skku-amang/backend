import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from core.models.generation import Generation


class Command(BaseCommand):
    help = "Create a superuser if none exists"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not email or not password:
            self.stdout.write(
                self.style.ERROR("Superuser environment variables are not set. Skipping.")
            )
            return
        
        try:
            if not User.objects.filter(email=email).exists():
                default_generation, created = Generation.objects.get_or_create(order=1)
                User.objects.create_superuser(email=email, password=password, generation=default_generation)
                self.stdout.write(
                    self.style.SUCCESS(f"Superuser {email} created successfully.")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Superuser with email {email} already exists. Skipping.")
                )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error creating superuser: {e}"))
            return
