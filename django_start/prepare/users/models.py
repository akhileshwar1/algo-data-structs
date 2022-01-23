from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    Choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(max_length=1, choices=Choices)
    dob = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

