from django.contrib import admin
from comments.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'body', 'user',)

admin.site.register(Comment, CommentAdmin)
