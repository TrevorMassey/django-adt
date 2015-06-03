from django.contrib import admin
from activityfeed.models import FeedItem, FeedPost

class FeedItemAdmin(admin.ModelAdmin):
    list_display = ('type', 'user', 'created', 'is_deleted')
    list_filter = ('type', 'created', 'is_deleted')

class FeedPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created',)

admin.site.register(FeedItem, FeedItemAdmin)
admin.site.register(FeedPost, FeedPostAdmin)