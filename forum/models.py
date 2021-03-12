# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=500)
    last_updated = models.DateField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.PROTECT)
    starter = models.ForeignKey(User, related_name='topics', null=True, on_delete=models.SET_NULL)


class Post(models.Model):
    message = models.TextField(max_length=3000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.PROTECT)
    created_when = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', null=True, on_delete=models.SET_NULL)
    updated_when = models.DateField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.SET_NULL)
