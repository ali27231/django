from django.contrib import admin

from message_box.models import Message
from posts.models import Post, Comment, Follow, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Tag)