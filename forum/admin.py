from django.contrib import admin
from .models import UserProfile, Board, Topic, Post
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)
