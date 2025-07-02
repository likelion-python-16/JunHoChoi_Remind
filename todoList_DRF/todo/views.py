from ast import Delete
from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView ,CreateView,DetailView,UpdateView
from django.urls import reverse_lazy


def todo_list(request):  #테스트용
    todo =Todo.objects.all()
    return render(request, 'todo/list.html', {"todos": todo}) 


# 전체보기
class TodoListViews(ListView): #제너릭뷰  
    model = Todo
    template_name = "todo/list.html"
    context_object_name = "todos"
    ordering = ["-created_at"]  
    #success_url = reverse_lazy("todo_List")
    
    
# 생성    
class TodoCreateViews(CreateView): #제너릭뷰  
    model = Todo
    template_name = "todo/create.html"
    fields = ['name', 'description', 'complete', 'exp']    
    print("=========================생성 ================")
    success_url = reverse_lazy("todo_List")


class TodoDetailViews(DetailView): #제너릭뷰  
    model = Todo
    template_name = "todo/detail.html"
    context_object_name = "todo"


class TodoUpdateViews(UpdateView): #제너릭뷰
    model = Todo
    fields = ['name', 'description', 'complete', 'exp']
    template_name = "todo/update.html"  
    context_object_name = "todo"
    success_url = reverse_lazy("todo_List")
    
    
    
