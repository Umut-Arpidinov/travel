from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    email = models.EmailField('email adress', unique=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pic', default='default.jpg')

    def __str__(self):
        return f'{self.username}'
    
