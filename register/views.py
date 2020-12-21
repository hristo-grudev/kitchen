from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from register.forms import RegisterForm


def register_user(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm()
        }
        return render(request, 'register.html', context)
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # add user
            login(request, user)  # login user
            return redirect('register user')

        context = {
            'form': form
        }
        return render(request, 'register.html', context)


def login_user(request):
    username = 'baticho'
    password = 'Rali2230'
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect('home')
    return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('home')