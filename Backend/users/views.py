from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect, redirect

from Backend.settings import LOGOUT_REDIRECT_URL
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse
from django import forms


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Login',
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Register',
        'form': form
    }
    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return redirect(LOGOUT_REDIRECT_URL)
