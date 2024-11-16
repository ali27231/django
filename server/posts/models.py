from django.db import models
from django.contrib.auth.models import User


# Create your models here

#
class Tag(models.Model):
    subject = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0, blank=True)


class Follow(models.Model):
    follower = models.ManyToManyField(User)
