from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CommentLikeViewSet, LikeViewSet, BookmarkViewSet, CommentViewSet
from . import views  # ← 새로 작성할 views.py 참조

router = DefaultRouter()
router.register(r"likes", LikeViewSet, basename="likes")
router.register(r"bookmarks", BookmarkViewSet, basename="bookmarks")
router.register(r"comments", CommentViewSet, basename="comments")
router.register(r"commentlikes", CommentLikeViewSet, basename="commentlikes")


# r은 주소의 마지막을 표시한 것이며 규칙이 아닌 관습이다.

app_name = "interaction"


urlpatterns = [

    path("api/interaction/", include(router.urls)),     
    
   # ✅ 이 부분 추가
    path("interaction/todo/detail/<int:pk>/", views.todo_detail_with_interaction, name="todo_interaction_detail"),
]
