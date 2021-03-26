# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='', blank=True)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=250)

    def get_topics_count(self):
        return self.topics.count()

    def get_posts_count(self):
        count = 0
        for topic in self.topics.all():
            count += topic.posts
        return count

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

