from .serializers import TodoSerializer
from .models import Todo
from django.http import *
from rest_framework import generics

"""
✅ 3. Generics Mixin

"""


# ListCreate
class TodoGenericsListCreateAPI(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    


# ✅ RetrieveUpdateDestroyAPIView는 다음 HTTP 메서드 3개를 처리합니다:
# 메서드	설명	예시 URL
# GET	상세 조회	/todo/1/
# PUT	전체 수정	/todo/1/ + JSON 바디
# DELETE	삭제	/todo/1/

class TodoGenericsRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()     # 어디서 데이터를 가져올지
    serializer_class = TodoSerializer # 데이터를 어떻게 직렬화할지
    
    
    
    
    