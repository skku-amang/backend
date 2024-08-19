# 베이스 이미지 설정
FROM python:3.11

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . /app/

# 서버 실행 명령어
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main.wsgi:application"]
