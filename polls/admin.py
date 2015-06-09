from django.contrib import admin
from polls.models import Poll, Item, Vote

class PollAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('answer',)


class VoteAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Poll, PollAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Vote, VoteAdmin)
