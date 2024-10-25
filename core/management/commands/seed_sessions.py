from django.core.management.base import BaseCommand

from core.models.session import Session


class Command(BaseCommand):
    help = f"밴드 기본 세션({', '.join(Session.NAME_CHOICES)}) 생성"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating default sessions...")
        for name in Session.NAME_CHOICES:
            if not Session.objects.filter(name=name).exists():
                Session.objects.create(name=name)
                self.stdout.write(
                    self.style.SUCCESS(f"Session {name} created successfully.")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Session {name} skipped as it is already exists."
                    )
                )
