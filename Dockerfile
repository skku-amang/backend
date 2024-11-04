FROM python:3.11

WORKDIR /app

# requirements.txt 파일을 복사하고 종속성을 설치합니다.
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드를 복사합니다.
COPY . /app/

# Django 애플리케이션 설정 스크립트를 실행합니다.
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# 포트를 노출합니다.
EXPOSE 8000

# 애플리케이션을 실행합니다.
CMD ["python", "-O", "manage.py", "runserver", "0.0.0.0:8000"]