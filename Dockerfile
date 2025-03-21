FROM python:3.11-slim AS builder

WORKDIR /app

# 빌드 의존성 설치 - pkg-config와 libdbus-1-dev 추가
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  gcc \
  python3-dev \
  libpq-dev \
  pkg-config \
  libdbus-1-dev \
  file \
  && rm -rf /var/lib/apt/lists/*

# Pip 패키지 설치
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt

# 런타임 이미지
FROM python:3.11-slim

WORKDIR /app

# 런타임 라이브러리 설치 - libdbus-1-3 추가
RUN apt-get update && apt-get install -y --no-install-recommends \
  libpq5 \
  libdbus-1-3 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Wheel 파일에서 패키지 설치
COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels

COPY . /app

# 보안을 위해 루트가 아닌 사용자로 실행
RUN useradd -m appuser
USER appuser

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main.wsgi:application"]