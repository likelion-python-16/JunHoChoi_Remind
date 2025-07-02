# 🚀 Fly.io 위의 Django/형식 Python 프로젝트 배포 전체 정보 (Windows + WSL 기반)




---

## ✅ 1. Fly.io CLI (‘flyctl’) 설치 (Windows)

### ▶ PowerShell 통해 설치:

```powershell
pwsh -Command "iwr https://fly.io/install.ps1 -useb | iex"
```

설치 후 출력 예상:

```
flyctl was installed successfully to C:\Users\YOUR_NAME\.fly\bin\flyctl.exe
```

### ▶ 시스템 PATH 환경변수가 다음과 같지 않으면 'flyctl' 명령을 인식하지 못합니다:

현재 확인:

```powershell
flyctl version
```

인식되지 않는다면 메뉴 > 경로 > `C:\Users\YOUR_NAME\.fly\bin` 가 `PATH` 환경값에 규가되어야 합니다.

---

## ✅ 1-2. Fly.io CLI (‘flyctl’) 설치 (WSL/Linux)

WSL (Ubuntu 등) 환경에서는 다음 명령으로 설치합니다:

```bash
curl -L https://fly.io/install.sh | sh
```

설치 후 `~/.fly/bin` 가 생성됩니다.

### ▶ PATH 값 일시 추가 (WSL 현재 키 중)

```bash
export PATH="$HOME/.fly/bin:$PATH"
```

### ▶ 영구 환경변수 등록:

```bash
echo 'export PATH="$HOME/.fly/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

(또는 `~/.zshrc` 사용 자원의 경우 `zsh` 개별 체크)

이후:

```bash
flyctl version
flyctl auth login
```

---

## ✅ 2. Fly.io 프로젝트 시작: `flyctl launch`

토큰크럼 또는 VSCode Terminal에서 하세요:

```bash
flyctl launch
```

진행 시 나오는 질문와 책임있는 선택지:


🟥 기본값으로 이미지 처럼 확인 버튼 클릭


![기본값으로확인버트클릭](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiK2bkltTooiEA0hAa56AGbLmK7Kgj11aTZuVUI2AOphLcXyseTawGEDqlIHhQ9X2zMWJa4CRFr-yBqepqc2Rv2M5KFNqMG5fr-MToVcHP_wo0_fAu_Y2UXFCUjaUBXTKOylJdr3Mg-4ZHN0CqYqinfNjlxKY8edQsgHudmUtnuvylPH4WZ1dy5XXrM37-f/w258-h640/2025-06-27%2016%2002%2052.png)




### 🟥 상세  CLI 설명

### 1. “App Name” 입력?

```
? App Name (leave blank to let us generate one):
```

* 그리고 연터: Fly.io가 드롭 이름 생성
* 또는 자기가 원하는 이름 입력 가능

✅ 첫 번째는 복사 위해 그리고 연터 해도 무리 X

### 2. 지역 선택

```
? Select region: nrt (Tokyo) or sin (Singapore) ...
```

* 한국에서 접속시 `nrt` (도쿄) 최고

✅ `nrt` 권고

### 3. PostgreSQL DB 설치?

```
? Would you like to set up a PostgreSQL database now?
```

* 테스트용은 `No`
* 실상 메이너 보기는 `Yes`

✅ 초기에는 `No` 권고

### 4. Dockerfile 자동 생성

* `Dockerfile`이 없을 경우 Fly.io가 자동 생성
* Django/DRF 가능 개별 Dockerfile은 후에 수정가능

✅ 자동 생성 해도 무리

### 5. 지금 배포할까요?

```
? Would you like us to deploy now?
```

* `Yes` 선택 시 `flyctl deploy` 자동 실행

✅ `Yes` 선택 권고

---

## ✅ 3. 배포 후 필요 행동

### ① .env 환경변수 설정

```bash
flyctl secrets set DJANGO_SECRET_KEY='...' DEBUG='False'
```

### ② Django STATIC 체치

```bash
python manage.py collectstatic
```

### ③ fly.toml 파일 확인

* 파이썬이 `8000` 포트 사용하면:

```toml
[env]
PORT = "8000"
```

### ④ 주소 확인

```
App deployed to https://your-app-name.fly.dev
```

---

## ✅ 요약 정보 정보

| 질문           | 기본값 OK? | 책임있는 회의          |
| ------------ | ------- | ---------------- |
| App 이름       | ✅       | 연터 또는 입력         |
| 지역 선택        | ❌       | `nrt (Tokyo)` 권고 |
| PostgreSQL 건 | ✅       | 초기에는 `No`        |
| 배포 여부        | ✅       | `Yes` 권고         |

---


✅  flyctl 명령어 사용 팁
```bash
로그인: flyctl auth login
새 프로젝트 시작: flyctl launch
앱 배포: flyctl deploy
상태 확인: flyctl status
```



### ✅ 슈퍼유저 생성 방법 (fly.io ssh 접속 후 createsuperuser)
```bash
flyctl ssh console          # 이미 접속 완료 상태

# 마이그레이션 먼저
python manage.py migrate


# 정적(static) 파일들을 한곳에 모아주는 Django의 명령어
python manage.py collectstatic --noinput

# 슈퍼유저 생성
python manage.py createsuperuser

```

이 작업을 마치면 /admin/ URL에서 관리자 로그인 가능합니다.


##### 추가설명
settings.py 파일에 다음과 같은 설정이 있다면:
```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
명령 실행 시:

```python
python manage.py collectstatic --noinput
```

✅ --noinput 옵션은?
일반적으로 Django는 “이전에 존재하는 파일을 덮어쓸까요?”를 물어봅니다.
--noinput은 질문 없이 자동으로 진행하도록 하는 옵션입니다.
배포 자동화 시 주로 사용됩니다.



---





## ✨ 필요할 수 있는 보조 파일 

### 1. Dockerfile 예시 (gunicorn 기반)


```dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PORT=8000

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "your_project_name.wsgi:application", "--bind", "0.0.0.0:8000"]

```
※ your_project_name 부분은 실제 Django 프로젝트 이름으로 교체 필요


### fly.toml 구조 예시
```toml
app = "your-app-name"

[build]
  image = "python:3.11-slim"

[env]
  PORT = "8000"

[[services]]
  internal_port = 8000
  protocol = "tcp"

  [[services.ports]]
    port = 80

  [[services.ports]]
    port = 443
```



### 3. .env.sample 결과 파일 

```ini
DJANGO_SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgres://user:password@host:port/dbname
ALLOWED_HOSTS=.fly.dev,yourdomain.com

```


### 4. settings.py 내 Fly 환경변수 대응 예시
```python
import os

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'fallback-secret-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# 정적 파일 처리
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
```





