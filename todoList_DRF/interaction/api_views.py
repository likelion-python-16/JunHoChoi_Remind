
from rest_framework import viewsets
from .models import Like, Bookmark, Comment, CommentLike
from .serializers import LikeSerializer, BookmarkSerializer, CommentSerializer 
from rest_framework import permissions
from rest_framework.decorators import action
from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework.response import Response
from .serializers import CommentLikeSerializer
from django.shortcuts import get_object_or_404


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all() # 좋아요의 전체 데이터
    serializer_class = LikeSerializer # 직렬화/역직렬화
    permisson_classes = [permissions.IsAuthenticated] #권한

    @action(detail=True, methods=["post"])
    def toggle(self, request, pk=None):
        todo = Todo.objects.get(pk=pk)
        user = request.user 
        like, created = Like.objects.get_or_create(todo=todo, user=user)
        like.is_like = not like.is_like
        like.save()
        serializer = TodoSerializer(todo, context={"request": request})
        return Response(serializer.data)
    
    
class BookmarkViewSet(viewsets.ModelViewSet): # 북마크 기능을 위한 ViewSet
    queryset = Bookmark.objects.all() 
    serializer_class = BookmarkSerializer 
    permission_classes = [permissions.IsAuthenticated] 

    @action(detail=True, methods=["post"]) 
    def toggle(self, request, pk=None): 
        todo = Todo.objects.get(pk=pk) 
        user = request.user

        bookmark, created = Bookmark.objects.get_or_create(todo=todo, user=user) 
        bookmark.is_marked = not bookmark.is_marked 
        bookmark.save() 

        serializer = TodoSerializer(todo, context={"request": request}) 
        return Response(serializer.data) 

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = None  # ← 페이지네이션 비활성화

    def get_queryset(self):
        todo_id = self.request.query_params.get("todo_pk")
        return Comment.objects.filter(todo_id=todo_id).order_by("-created_at")

    def perform_create(self, serializer):
        todo_id = self.request.data.get("todo_pk")
        todo = Todo.objects.get(pk=todo_id)
        serializer.save(user=self.request.user, todo=todo)

class CommentLikeViewSet(viewsets.ModelViewSet):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=True, methods=['post'])  # /commentlikes/{pk}/toggle/
    def toggle(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user
        like, created = CommentLike.objects.get_or_create(comment=comment, user=user)
        like.is_like = not like.is_like
        like.save()
        return Response({
            "is_liked": like.is_like,
            "like_count": CommentLike.objects.filter(comment=comment, is_like=True).count()
        })