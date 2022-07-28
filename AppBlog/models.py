from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.username+" "+str(self.email)

class Profile(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    image = models.ImageField()
    website = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name+" "+str(self.email)

class Post(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    body = models.CharField(max_length=150)
    author = models.CharField(max_length=30)
    date = models.DateField()
    image = models.ImageField()

    def __str__(self):
        return self.title+" "+str(self.date)