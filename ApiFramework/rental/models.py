from django.db import models
from django.contrib.auth import settings


# Create your models here.


class Friend(models.Model):
    name = models.CharField(max_length=200)


class Belonging(models.Model):
    name = models.CharField(max_length=200)


class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
