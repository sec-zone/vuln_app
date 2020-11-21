from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class BlogUser(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    password = models.CharField(max_length=256)

    def save(self, **kwargs):
        some_salt = '123' 
        self.password = make_password(self.password, some_salt)
        return super().save(**kwargs)

    def __str__(self):
        return self.username

class Email(models.Model):
    mail_from = models.CharField(max_length=256)
    subject = models.CharField(max_length=256)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject





