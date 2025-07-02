from django.urls import path ,include

from .custom_logout import CustomLogoutAPI
from . import views
from .api_api_views import *
from .api_generic_views import *
from .api_mixin_generics_views import *

#ViewSets 설정
from rest_framework.routers import DefaultRouter
from .api_viewset_router_views import TodoViewSet
router = DefaultRouter()
router.register("" , TodoViewSet, basename="todo")



app_name = "todo"  # 네임스페이스 지정
  
urlpatterns = [
  #path("list/", views.todo_list, name="todo_List"),
  
  
  #✅템플릿 Views
  #http://127.0.0.1:8000/todo/list/
  #http://127.0.0.1:8000/todo/create/  
  #http://127.0.0.1:8000/todo/detail/1
  #http://127.0.0.1:8000/todo/update/1
  path("list/", views.TodoListViews.as_view(), name="todo_List"),
  path("create/", views.TodoCreateViews.as_view(), name="todo_Create"),
  path("detail/<int:pk>/", views.TodoDetailViews.as_view(), name="todo_Detail"),  
  path("update/<int:pk>/", views.TodoUpdateViews.as_view(), name="todo_Update"),

 
  
  #1️⃣apiViews
  #http://127.0.0.1:8000/todo/api/list/
  #http://127.0.0.1:8000/todo/api/create/
  #http://127.0.0.1:8000/todo/retrieve/1/
  #http://127.0.0.1:8000/todo/api/update/1
  #http://127.0.0.1:8000/todo/api/delete/1
  path("api/list/",  TodoListAPI.as_view(), name="todo_api_list"),  
  path("api/create/", TodoCreateAPI.as_view(), name="todo_api_create"),  
  path("api/retrieve/<int:pk>/", TodoRetrieveAPI.as_view(), name="todo_api_retrieve"),
  path("api/update/<int:pk>/", TodoUpdateAPI.as_view(), name="todo_api_update"),
  path("api/delete/<int:pk>/", TodoDeleteAPI.as_view(), name="todo_api_delete"),
  

  
  #2️⃣GenericAPIView
  #http://127.0.0.1:8000/todo/generics/list/
  #http://127.0.0.1:8000/todo/generics/create/
  #http://127.0.0.1:8000/todo/generics/retrieve/1/
  #http://127.0.0.1:8000/todo/generics/update/1/
  #http://127.0.0.1:8000/todo/generics/delete/1
  path("generics/list/", TodoGenericsListAPI.as_view(), name="todo_generics_list"),
  path("generics/create/", TodoGenericsCreateAPI.as_view(), name="todo_generics_create"),
  path("generics/retrieve/<int:pk>/", TodoGenericsRetrieveAPI.as_view(), name="todo_generics_retrieve"),
  path("generics/update/<int:pk>/", TodoGenericsUpdateAPI.as_view(), name="todo_generics_update"),  
  path("generics/delete/<int:pk>/", TodoGenericsDeleteAPI.as_view(), name="todo_generics_delete"),
  
  
  
  #3️⃣GenericAPIView + Mixin ===> List + Create # Retrieve + Update + Delete (RUD)
  # 여기서 GET /mix_generics/list/와 POST /mix_generics/create/는 같은 View (ListCreateAPIView)
  # GET, PUT, DELETE 모두 /generics/<int:pk>/에서 처리 가능 (RetrieveUpdateDestroyAPIView)    
  #http://127.0.0.1:8000/todo/mixin_generics/
  #http://127.0.0.1:8000/todo/mixin_generics/1/ GET, PUT, DELETE 모두 처리
  path("mixin_generics/", TodoGenericsListCreateAPI.as_view(), name="todo_mixin_generics_list_create"),
  path("mixin_generics/<int:pk>/", TodoGenericsRetrieveUpdateDeleteAPI.as_view(), name="todo_mixin_generics_rud"),
  
  
  
  #4️⃣viewSets : CRUD을 한 클래스에 통합
  #http://127.0.0.1:8000/todo/viewsets/
  path("viewsets/", include(router.urls)),



  #✅logout API
  path("api/custom-logout/", CustomLogoutAPI.as_view(), name="custom-logout"),


]


