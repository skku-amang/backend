from django.core.management.base import BaseCommand

from core.models.generation import Generation


class Command(BaseCommand):
    help = f"밴드 기본 기수 25.0기부터 37.5기까지 생성"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating default generations...")

        # 25기부터 37기까지 생성
        generations = [x/2 for x in range(50, 76)]

        for order in generations:
            generation, created = Generation.objects.get_or_create(order=order)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Generation {order} created successfully."))
            else:
                self.stdout.write(f"Generation {order} skipped as it is already exists.")