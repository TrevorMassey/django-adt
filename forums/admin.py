from django.contrib import admin

# Register your models here.
from forums.models import Forum, Post, Topic

admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Post)
