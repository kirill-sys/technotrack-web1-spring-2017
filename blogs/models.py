# -- coding: utf-8 --
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    blog = models.ForeignKey(Blog, related_name='posts')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rate = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
