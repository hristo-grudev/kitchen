from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.shortcuts import render, redirect

from register.forms import RegisterForm, LoginForm, ProfileForm


@transaction.atomic  # изпълнява всички или нито една
def register_user(request):
    if request.method == 'GET':
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'register.html', context)
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()  # add user
            profile = profile_form.save(commit=False)  # не го запазва преди да направи връзката 1 към 1
            profile.user = user
            profile.save()

            login(request, user)  # login user
            return redirect('register user')

        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'GET':
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'login.html', context)
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        context = {
            'login_form': login_form
        }
        return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')