from django.db import models

# Create your models here.

class User(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.EmailField()
    user_contact=models.IntegerField()
    user_password=models.CharField(max_length=25)