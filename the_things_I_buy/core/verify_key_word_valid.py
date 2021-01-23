from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from the_things_I_buy_auth.models import UserKeyWord


def verify_key_word_valid(current_user, key_word):
    if current_user:
        user_key_word = UserKeyWord.objects.get(user=current_user)
        if not user_key_word.key_word == key_word:
            raise ValidationError("Key Word does not match your profile")
        else:
            return True
    else:
        raise ValidationError('The username does not match any of our profiles')

def verify_passwords(form):
    password1 = form.cleaned_data['password1']
    password2 = form.cleaned_data['password2']
    if not password1 == password2:
        raise ValidationError("Passwords don't match. Please try again.")
    else:
        return True