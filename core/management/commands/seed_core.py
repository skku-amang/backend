from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "초기 데이터를 생성합니다."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding...")
        try:
            call_command("seed_generations")
            call_command("seed_sessions")
            call_command("seed_test_performance")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Seeding failed: {e}"))
            raise  # 예외를 다시 발생시켜 배포 프로세스가 실패하도록 합니다.
        else:
            self.stdout.write(self.style.SUCCESS("Seeding completed successfully."))
