from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 자동 로그인
            return redirect("todo:todo_List")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})