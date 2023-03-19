from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=256)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
