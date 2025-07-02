from ast import Is
from re import search
from rest_framework import viewsets
from .pagination import CustomPageNumberPagination
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser


"""
✅ 4. ViewSet은
✅ ViewSet은 CRUD를 한 클래스에서 처리하며 Router와 함께 사용됨
✅ ViewSet 하나로 CRUD를 자동 처리 (GET, POST, PUT, DELETE)
"""


class TodoViewSet(viewsets.ModelViewSet):
    #queryset = Todo.objects.all().order_by('-created_at')  
    serializer_class = TodoSerializer
    
    #pagination
    pagination_class =CustomPageNumberPagination
    
    #인증
    authentication_classes = [SessionAuthentication]
    
    #권한
    permission_classes = [IsAuthenticated]
    
    #이미지
    parser_classes = [JSONParser,MultiPartParser, FormParser]
    
    
    # 검색기능
    filter_backends =[filters.SearchFilter]
    search_fields =['name', 'description']
    
    
    def get_queryset(self):
        qs =Todo.objects.all().order_by('-created_at')
        print("🤬 정렬된 queryset preview", list(qs[:3]) ," 🌟 :: ") #서버 로그 확인용
        return qs
    
    
            
    
    