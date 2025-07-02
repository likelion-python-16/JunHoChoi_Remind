# 📝 Django REST Framework Todo API 프로젝트

간단한 Todo API를 구현한 Django REST Framework(DRF) 기반의 학습용 프로젝트입니다. 이 프로젝트는 API 설계, 직렬화, 뷰셋, 라우팅 등 DRF의 기본 개념을 실습하는 데 초점을 맞춥니다.


---

![이미지](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiam-3oMKCofzrcmRmwjoEU8BAbaUdI-6je0JvicSwlU42sOr8XCaS70PItkK4tIi29M1z_g35pqELO8HWZXzs9oiZ3wrzO4kw-VvFKs5GRGdj40449nEEUDp3EipUOHzFf9FGLYu2OXWukAeRlLon5pQtQz_5uBq0zxg4KDcuqiBMOjaqRzmOgTnFHQMeI/s2296/2025-07-02%2013%2015%2022.png)

![이미지](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1V8dmCiyLBHyLZ4bcW03Ubrlgu-ZyPBZFkxfc9K3fBWK6EEQyRZDWknjzXP3lIncIrBQFbEXb1jy2HkPqHjOICBNiO_GFYCvDgVqmbqCV8Nj6J-gZ43WK8wDi0uGoxBIbSlCC9W0bF0ykZb90PXHigKjNd9KNpPletaFTls19iGgs5ttat5LN61jszUhe/s1371/2025-07-02%2013%2016%2044.png)


![이미지](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi12vpt9j686hALWqKRkVYB_FIp93UJcb1U3aubWNOI996SJMRSPkRkZCJZwutwwTG5Xkb_tgcJ5FZZBjPDNYKour3vNgfnVprW_QzqEjffN8mSCUhUun0oiPUIIdCxd7SqJ5Q9JN_3R4902SA_KLggWdzKNdxqoB6I394ot4Nc1AzdZtdQ3H5bXgyqBc5C/s1858/2025-07-02%2013%2016%2024.png)


## 🔖프로젝트 구조
```bash

todoList_DRF/
├── .github/
├── config/                      # 프로젝트 설정 (settings, urls 등)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── interaction/                # 앱 1: interaction
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── api_views.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── todo/                       # 앱 2: todo (기능별로 파일 분리)
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── api_api_views.py
│   ├── api_generic_views.py
│   ├── api_mixin_generics_views.py
│   ├── api_viewset_router_views.py
│   ├── apps.py
│   ├── custom_logout.py
│   ├── models.py
│   ├── pagination.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── media/                      # 업로드 파일 저장 경로
├── static/                     # 정적 파일(css, js 등)
├── templates/                  # 템플릿 디렉토리
│   ├── interaction/
│   ├── registration/
│   ├── todo/
│   ├── base.html
│   ├── footer.html
│   ├── head.html
│   ├── header.html
│   └── index.html
│
├── .dockerignore
├── .env                        # 환경 변수
├── .gitignore
├── db.sqlite3                  # SQLite DB (로컬용)
├── Django(todoList) 7 배포.md  # 배포 관련 문서
├── Dockerfile                  # 도커 설정
├── fly_deploy_method.md        # Fly.io 배포 가이드
├── fly.toml                    # Fly.io 설정 파일
├── manage.py
├── README.md
└── requirements.txt            # 의존성 목록

```

### 🧩 interaction 앱의 주요 기능

좋아요 (Like): 사용자가 특정 todo 또는 콘텐츠에 좋아요를 누를 수 있음

북마크 (Bookmark): 관심 있는 todo를 북마크하여 나중에 쉽게 확인 가능

댓글 (Comment): 사용자 간 커뮤니케이션 또는 메모용 댓글 기능 제공



## ⚙️ 개발 환경

* Python 3.12.3
* Django 5.2.1
* Django REST Framework
* 가상환경: `venv` 사용

---

## ⭕ 프로젝트 생성
### 1.시작하기
```bash
mkdir todoList_DRF  #루트 폴더 따로, 설정 폴더 따로
cd todoList_DRF    
django-admin startproject config .   # 현재 디렉토리에 장고 프로젝트 시작하기
python manage.py startapp todo   # todo 앱 생성
```

### 2.앱 등록 (settings.py 수정)
```python
INSTALLED_APPS = [
    ...
    'todo',
    'rest_framework',  # DRF 사용 시
]
```
### 3. 마이그레이션 적용  && superuser 생성 && 개발 서버 실행
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 4.추가적으로 할 것
1. todo/admin.py에서 모델 Todo 등록
2. todo/models.py에 모델 정의
3. urls.py를 todo/urls.py, config/urls.py로 나누고 include 설정


---


## ▶️ 실행 방법

1. 가상환경 활성화

```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

2. 패키지 설치

```bash
pip install -r requirements.txt

# Windows PowerShell 전용:
$env:PYTHONUTF8=1; pip install -r requirements.txt
```

3. 서버 실행

```bash
python manage.py runserver
```

---

## 📆 데이터베이스 마이그레이션

```bash
# 모델 변경 사항 생성
python manage.py makemigrations

# 실제 DB에 반영
python manage.py migrate

# 반영 내역 확인
python manage.py showmigrations
```

> 새 앱 생성 시:

```bash
python manage.py startapp api
```

---




## 🧹 마이그레이션 초기화 (선택적)

```bash
rm -f db.sqlite3
rm -r api/migrations
python manage.py makemigrations api
python manage.py migrate
python manage.py createsuperuser
```

---

## ✅ Django 모델 시각화

### 1. 패키지 설치

```bash
pip install django-extensions pydot
```

### 2. `settings.py` 설정

```python
INSTALLED_APPS = [
    ...
    'todo',
    'rest_framework',  # DRF 사용 시
]
```

### 3. `.dot` 파일 생성

```bash
python manage.py graph_models api > models.dot
```

> `api`는 시각화할 앱 이름입니다.

### 4. Graphviz 설치

* 다운로드: [https://graphviz.org/download/](https://graphviz.org/download/)
* 설치 후 `dot` 명령어가 터미널에서 인식되어야 함

### 5. `.dot` 파일을 이미지로 변환

```bash
dot -Tpng models.dot -o models.png
```

> 생성된 `models.png`로 모델 관계를 시각적으로 확인할 수 있습니다.

### 🔍 온라인 시각화 도구

* [Graphviz Visual Editor](https://edotor.net/)
* [Viz.js Online](https://dreampuf.github.io/GraphvizOnline/?engine=dot)

---

## 📦 Commit 메시지 컨벤션 (Conventional Commits)

명확하고 일관된 Git 기록 작성을 위해 [Conventional Commits](https://www.conventionalcommits.org/) 형식을 따릅니다.

### 📌 타입 예시

| 타입         | 설명                |
| ---------- | ----------------- |
| `feat`     | 새로운 기능 추가         |
| `fix`      | 버그 수정             |
| `docs`     | 문서 수정 (README 등)  |
| `style`    | 코드 포맷팅 (기능 변화 없음) |
| `refactor` | 리팩토링 (기능 변화 없음)   |
| `test`     | 테스트 코드 추가/수정      |
| `chore`    | 기타 설정 변경 등        |

### 💡 예시 커밋

```bash
git commit -m "feat: Todo 목록 조회 API 구현"
git commit -m "fix: 날짜 형식 오류 수정"
git commit -m "docs: README 업데이트"
git commit -m "style: 불필요한 공백 제거"
git commit -m "refactor: view 함수 분리"
git commit -m "test: Todo 생성 테스트 추가"
git commit -m "chore: requirements.txt 정리"
```

---

## 🔑 관리자 계정 생성

```bash
python manage.py createsuperuser
```

---


##### 배포
```bash
curl -L https://fly.io/install.sh | sh

```


##### Fly 배포용 ALLOWED_HOSTS 설정
```bash
APP_NAME = os.environ.get("FLY_APP_NAME")
ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev", "localhost", "127.0.0.1"]
```

✅  flyctl 명령어 사용 팁
```bash
로그인: flyctl auth login
새 프로젝트 시작: flyctl launch
앱 배포: flyctl deploy
상태 확인: flyctl status
```


## 👨‍💻 Author

**코담(Codam)**
👩‍🏫 이유정
👉 [https://codam.kr](https://codam.kr)
