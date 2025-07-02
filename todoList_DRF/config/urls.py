from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.shortcuts import redirect

from django.conf import settings
from django.conf.urls.static import static

# ✅ JWT 뷰 임포트
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("todo/", include("todo.urls")),
    path("", lambda request:redirect("todo:todo_List") ),
    path("api-auth/", include("rest_framework.urls")  , name="login"),
    
    path("accounts/", include("django.contrib.auth.urls")),  # 기본 인증
    path("accounts/", include("accounts.urls")),              # 회원가입 추가
    
    
    
    # ✅ JWT 로그인/리프레시 추가
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),       # 로그인
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    
    path("", include("interaction.urls"))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



