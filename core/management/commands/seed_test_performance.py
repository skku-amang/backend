from django.core.management.base import BaseCommand

from core.models.performance import Performance


class Command(BaseCommand):
    help = f"테스트용 공연 생성"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating test performances...")

        if Performance.objects.count() > 0:
            self.stdout.write(
                self.style.WARNING(
                    "Performance already exists. Skipping creating test performances."
                )
            )
            return

        TEST_PERFORMANCE_NAME = "2024년 2학기 정기공연"
        if not Performance.objects.filter(name=TEST_PERFORMANCE_NAME).exists():
            Performance.objects.create(
                name=TEST_PERFORMANCE_NAME,
                description="테스트용 공연입니다.",
                location="동방",
                startDatetime="2024-11-01T19:00:00Z",
                endDatetime="2024-11-01T21:00:00Z",
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Performance {TEST_PERFORMANCE_NAME} created successfully."
                )
            )
        else:
            self.stdout.write(self.style.WARNING(
                f"Performance {TEST_PERFORMANCE_NAME} skipped as it is already exists."
            ))
