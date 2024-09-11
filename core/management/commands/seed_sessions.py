from django.core.management.base import BaseCommand

from core.models.session import Session


class Command(BaseCommand):
    help = "밴드 기본 세션(보컬, 기타, 베이스, 드럼, 신디) 생성"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating default sessions...")
        for name in Session.NAME_CHOICES:
            if not Session.objects.filter(name=name).exists():
                Session.objects.create(name=name)
                self.stdout.write(
                    self.style.SUCCESS(f"Session {name} created successfully.")
                )
            else:
                self.stdout.write(self.style.WARNING(f"Session {name} already exists."))
