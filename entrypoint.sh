#!/bin/bash
set -e

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate

echo "Creating superuser if needed..."
python manage.py create_superuser || echo "Superuser may already exist."

# Django 초기 데이터 로드
echo "Loading initial data..."
python manage.py seed_sessions || echo "Initial data already loaded."

echo "Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:8000 main.wsgi:application