from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=254,unique=True)
    identityAccessKey = models.CharField(max_length=200)
    status = models.CharField(max_length=10)
