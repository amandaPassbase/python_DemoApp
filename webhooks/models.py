from django.db import models

class User(models.Model):
    identityAccessKey = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    status = models.CharField(max_length=10)
