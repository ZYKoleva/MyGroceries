from django.contrib.auth.models import User
from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to='images', blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    customized_prod = models.BooleanField(default=True)
    counter = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class MyProducts(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)