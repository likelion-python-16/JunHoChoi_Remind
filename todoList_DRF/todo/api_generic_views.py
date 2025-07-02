from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.response import Response
from rest_framework import status
from django.http import *
from rest_framework import generics

"""
✅ 2. GenericAPIView (rest_framework.generics.GenericAPIView)

📌 특징: APIView를 확장한 클래스
queryset, serializer_class 속성 사용 가능
get_object(), get_queryset(), get_serializer() 등 재사용 가능한 메서드 제공
mixin 클래스들과 함께 사용하는 것이 일반적
REST API의 **패턴화된 작업(CRUD)**을 쉽게 처리 가능


✅ 단독 사용은 잘 안 하고, 보통 믹스인과 함께 씀:
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin


✅단순한 CRUD → GenericAPIView + mixin 또는 ListCreateAPIView 같은 단축형 사용
"""

# DRF_GenericAPIView


# list
class TodoGenericsListAPI(generics.ListAPIView):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer


# create
class TodoGenericsCreateAPI(generics.CreateAPIView):
    serializer_class = TodoSerializer


# retrieve(상세조회)
class TodoGenericsRetrieveAPI(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class=TodoSerializer
    

# update(수정)
class TodoGenericsUpdateAPI(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class=TodoSerializer
    
# delete
class TodoGenericsDeleteAPI(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class=TodoSerializer
    
 
    
    
    