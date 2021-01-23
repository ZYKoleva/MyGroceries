from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from the_things_I_buy_auth.models import UserKeyWord


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))




class RegisterForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Потребителско име', min_length=4, max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Въведи парола')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Потвърди паролата')
    key_word = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Key Word', min_length=4, max_length=50)

    def clean_username(self):
        username = self.cleaned_data['username']
        result = User.objects.filter(username=username)
        if result.count():
            raise ValidationError("Username is already taken. Please chose another one.")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match. Please try again.")

        return password2

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
        )
        return user


class ResetPswForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Потребителско име',
                               min_length=4, max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Въведи парола')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Потвърди паролата')
    key_word = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='KeyWord')
    #
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     result = User.objects.filter(username=username)
    #     if result.count() == 0:
    #         raise ValidationError("Username does not match any of the profiles")
    #     return username
    #
    # def clean_key_word(self):
    #     key_word = self.cleaned_data['key_word']
    #     user_key_word = UserKeyWord(key_word=key_word)
    #     username = self.cleaned_data['username']
    #     result = User.objects.filter(username=username)
    #     if
    #
    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Passwords don't match. Please try again.")
    #
    #     return password2
    #
    # def save(self):
    #     user = User.objects.create_user(
    #         username=self.cleaned_data['username'],
    #         password=self.cleaned_data['password1'],
    #     )
    #     return user


