from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.shortcuts import render

from the_things_I_buy_auth.forms import LoginForm, RegisterForm


def login_user(request):
    if request.method == "GET":
        context = {
            'login_form': LoginForm()
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
                return redirect('load home page')
            else:
                context = {
                    'wrong_credentials': 'Username and/or password don\'t match. Please try again.',
                    'login_form': login_form
                }
                return render(request, 'login.html', context)
        else:
            return render(request, 'login.html', {'login_form': login_form})


def register_user(request):
    if request.method == 'GET':
        context = {
            'register_form': RegisterForm()
        }
        return render(request, 'register.html', context)
    else:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            # group = Group.objects.get(name='Registered')
            # group.user_set.add(user)
            login(request, user)
            return redirect('load home page')
        else:

            context = {
                'register_form': register_form,
            }
            if 'username' in register_form.errors.keys():
                context['username_error'] = register_form.errors['username']
            if 'password2' in register_form.errors.keys():
                context['passwords_error'] = register_form.errors['password2']
            return render(request, 'register.html', context)


def logout_user(request):
    logout(request)
    return redirect('load home page')


