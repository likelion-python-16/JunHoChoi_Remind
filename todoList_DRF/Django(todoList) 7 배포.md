1. Fly.io 계정 및 CLI 준비
- 계정 생성
https://fly.io 에 접속 → “Sign up”
GitHub/이메일로 가입 → 이메일 인증 완료

- macOS/Linux:
```
curl -L https://fly.io/install.sh | sh
```

- 로그인:
```
flyctl auth login
```
- 브라우저가 열리면 Fly.io 계정으로 로그인

- (기존 앱 삭제) 연습용 리셋:
```
flyctl apps list
flyctl apps destroy 자신의 앱이름
```

- settings.py 업데이트:
```
import os

# 배포용 SECRET_KEY
SECRET_KEY = os.environ.get("SECRET_KEY", "<로컬용-디폴트키>")

# 도메인 허용
APP_NAME = os.environ.get("FLY_APP_NAME", "")
ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev"]

# CSRF 보호
CSRF_TRUSTED_ORIGINS = [f"https://{APP_NAME}.fly.dev"]

# 정적 파일 수집
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```

- fly launch 실행:
```
flyctl launch
```

- 환경 변수(Secrets) 설정확인(settings.py, .env)

- 배포 명령 실행:
```
flyctl deploy
```

- SSH 접속하여 마이그레이션:
```
flyctl ssh console
# 쉘이 root@컨테이너ID:/app 로 변경되면
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
exit
```

- 결과 확인
- 코드 수정 후 다시 배포할 때마다:
```
flyctl deploy
```