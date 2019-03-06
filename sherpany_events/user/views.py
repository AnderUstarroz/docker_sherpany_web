from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login as user_login, authenticate, logout as user_logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'user/index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_login(request, form.user)
            return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            user_login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()

    return render(request, 'user/register.html', {'form': form})


def logout(request):
    user_logout(request)
    return redirect('index')
