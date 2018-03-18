from django.db import models


class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")