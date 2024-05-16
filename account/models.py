from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    email = models.EmailField('email adress', unique=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pic', default='default.jpg')

    def __str__(self):
        return f'{self.username}'
