from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect


from the_things_I_buy.core.verify_key_word_valid import verify_key_word_valid, verify_passwords
from the_things_I_buy_auth.forms import LoginForm, RegisterForm, ResetPswForm
from the_things_I_buy_auth.models import UserKeyWord


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
            key_word = register_form.cleaned_data['key_word']
            userkeyword = UserKeyWord(key_word=key_word, user=user,)
            userkeyword.save()
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


def reset_password(request):
    if request.method == 'GET':
        context = {
            'reset_form': ResetPswForm()
        }
        return render(request, 'reset_psw.html', context)
    else:
        reset_psw_form = ResetPswForm(request.POST)
        if reset_psw_form.is_valid():
            username = reset_psw_form.cleaned_data['username']
            key_word = reset_psw_form.cleaned_data['key_word']
            current_user = User.objects.get(username=username)
            try:
                is_key_word_valid = verify_key_word_valid(current_user, key_word)
                if is_key_word_valid:
                    are_psw_valid = verify_passwords(reset_psw_form)
                    if are_psw_valid:
                        new_psw = reset_psw_form.cleaned_data['password2']
                        hashed_psw = make_password(new_psw)
                        current_user.password = hashed_psw
                        current_user.save()
                        return redirect('login')
            except ValidationError as ex:
                context = {
                    'error_msg': ex.message,
                    'reset_form': reset_psw_form
                }
                return render(request, 'reset_psw.html', context)

        else:
            context = {
                'reset_form': reset_psw_form
            }
            return render(request, 'reset_psw.html', context)

