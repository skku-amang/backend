# What is this repo about?
아망 홈페이지 프로젝트를 위한 백엔드 서버입니다.


# 준비물
- git: https://git-scm.com/downloads
- python >= 3.10
- virtualenv: https://pypi.org/project/virtualenv/
- postgresql: https://www.postgresql.org/download/

# 사용법
## 1. 이 레포지토리를 클론합니다.
```bash
git clone https://github.com/skku-amang/backend
```

## 2. 가상환경을 설정합니다.
```bash
cd backend
virtualenv env
source env/bin/activate
```

## 3. 필요한 라이브러리를 설치합니다.
```bash
pip install -r requirements.txt
```

## 4. PostgreSQL 설치 및 초기화(ubuntu 기준)
### 4-1. PostgreSQL 설치 및 실행
```bash
sudo apt-get update                         # 패키지 업데이트
sudo apt-get install postgresql             # postgresql 설치
sudo service postgresql start               # postgresql 서비스 시작
```

### 4-2. PostgreSQL 초기화
```bash
sudo -u postgres psql                       # 기본 사용자(postgres)로 psql 실행
ALTER USER postgres PASSWORD <새 비밀번호>;  # postgres 사용자 비밀번호 변경
sudo service postgresql restart             # postgresql 서비스 재시작
\q                                          # psql 종료
```
위에서 설정한 <새 비밀번호>를 `.env.local` 파일에 `DATABASE_PASSWORD`로 설정합니다.


## 5. DB 초기화
```bash
python manage.py migrate
```


## 6. 디버그 서버 실행
```bash
python manage.py runserver
```
또는 `F5`를 눌러 vscode 세팅을 이용하여 디버그 서버를 실행할 수 있습니다.
