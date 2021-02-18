from django.db import models

class Verification(models.Model):
    email = models.EmailField(max_length=254,unique=True)
    identityAccessKey = models.CharField(max_length=200)
    status = models.CharField(max_length=10)

