from django.contrib.auth.models import User
from django.db import models


class UserKeyWord(models.Model):
    key_word = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)







