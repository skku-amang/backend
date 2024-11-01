#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

def load_environment_variables():
    """
    환경 변수를 우선순위에 맞게 로드합니다.   
    최종 적용 환경 변수는 다음과 같습니다.   
    (겹치는 변수가 있을 경우 순번이 낮은 파일의 변수가 최종적으로 적용됩니다.)
    1. .env.local(gitignore에 등록되기에 직접 생성해야 합니다.)
    2. .env.development
    3. .env.production
    4. .env
    """
    loaded_env_files = []

    if os.path.exists('.env.local'):
        load_dotenv('.env.local')
        loaded_env_files.append('.env.local')

    if os.path.exists('.env.development') and os.getenv('DJANGO_SETTINGS_MODULE') == 'main.settings.development':
        load_dotenv('.env.development')
        loaded_env_files.append('.env.development')

    if os.path.exists('.env.production') and os.getenv('DJANGO_SETTINGS_MODULE') == 'main.settings.production':
        load_dotenv('.env.production')
        loaded_env_files.append('.env.production')

    if os.path.exists('.env'):
        load_dotenv('.env')
        loaded_env_files.append('.env')

    logger.info(f"Loaded {', '.join(loaded_env_files)}")
    print(f"Loaded {', '.join(loaded_env_files)}")


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings.development")    # TODO: 환경변수에 따라 설정 변경
    load_environment_variables()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
