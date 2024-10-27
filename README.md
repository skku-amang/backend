# 레포지토리 소개
아망 홈페이지 프로젝트를 위한 백엔드 서버입니다.


# 레포지토리 구조
```
backend/
├── .ebextensions          # AWS Elastic Beanstalk 배포 스크립트: AWS에서의 CI/CD
├── .github                # GitHub Actions 설정: on-premise CI/CD
├── .vscode                # vscode 설정: 디버깅 설정, 코드 포맷터 설정, 마이그레이션 스크립트 등
├── core                   # 핵심 앱
│   ├── management         # 커맨드 스크립트: seed 데이터 추가
│   ├── migrations         # 마이그레이션 파일
│   ├── models             # 모델 정의
│   ├── serializers        # 시리얼라이저 정의: DTO 역할
│   ├── views              # 뷰 정의: Controller 역할
│   ├── admin.py           # 어드민 설정: Django 내장 어드민 페이지
│   ├── apps.py            # 앱 설정
│   ├── middleware.py      # 미들웨어 설정
│   ├── permissions.py     # 권한 설정
│   └── urls.py            # URL 설정
├── main                   # 메인 앱
│   ├── settings           # 설정 파일
│   │   ├── base.py        # 기본 설정
│   │   ├── development.py # 개발 설정: base.py를 상속
│   │   └── production.py  # 배포 설정: base.py를 상속
│   ├── static             # 정적 파일
│   ├── asgi.py            # URL 설정: 비동기 서버 설정
│   ├── urls.py            # URL 설정: 각 앱의 모든 URL 매핑
│   └── wsgi.py            # WSGI 설정: 동기 서버 설정, 일반적으로 배포 환경에서 사용
├── templates              # 템플릿 파일: 홈페이지 템플릿
├── user                   # 유저, 인증 앱: core 앱과 구조 동일
├── .env.development       # 개발 환경 설정 파일
├── .flake8                # 코드 포맷터 설정
├── .gitignore             # git 무시 파일 설정
├── Dockerfile             # Docker 설정
├── manage.py              # Django CLI
├── README.md              # 레포지토리 소개
└── requirements.txt       # 필요한 라이브러리 목록
```

# 레포지토리 세팅
## 준비물
- git: https://git-scm.com/downloads
- python >= 3.10: https://www.python.org/downloads/
- virtualenv: https://pypi.org/project/virtualenv/
- postgresql: https://www.postgresql.org/download/


## 사용법
### 1. 이 레포지토리를 클론합니다.
```bash
git clone https://github.com/skku-amang/backend
```

### 2. 가상환경을 설정합니다.
```bash
cd backend
sudo apt install python3-virtualenv
virtualenv .env
source .env/bin/activate
```

### 3. 필요한 라이브러리를 설치합니다.
```bash
pip install -r requirements.txt
```

### 4. PostgreSQL 설치 및 초기화(ubuntu 기준)
#### 4-1. PostgreSQL 설치 및 실행
```bash
sudo apt-get update                         # 패키지 업데이트
sudo apt-get install postgresql             # postgresql 설치
sudo service postgresql start               # postgresql 서비스 시작
```

#### 4-2. PostgreSQL 초기화
아래에서 설정할 `<새 비밀번호>`를 `.env.local` 파일에 `DATABASE_PASSWORD`로 설정합니다.
데이터베이스 유저와 데이터베이스 이름은 기본 값인 `postgres`를 사용합니다.
```bash
sudo -u postgres psql                       # 기본 사용자(postgres)로 psql 실행
ALTER USER postgres PASSWORD <새 비밀번호>;  # postgres 사용자 비밀번호 변경
sudo service postgresql restart             # postgresql 서비스 재시작
\q                                          # psql 종료
```


### 5. DB 마이그레이션 및 시드 데이터 추가
```bash
python manage.py migrate
python manage.py seed_core
python manage.py create_superuser
```


### 6. 디버그 서버 실행
```bash
python manage.py runserver
```
또는 `F5`~~딸깍~~를 눌러 vscode 세팅을 이용하여 디버그 서버를 실행할 수 있습니다.
