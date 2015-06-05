from django.contrib import admin
from games.models import Game, Chapter, ChapterMember

class GameAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('game', 'open_date', 'launch_date', 'close_date')

class ChapterMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'join_date', 'leave_date')

admin.site.register(Game, GameAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(ChapterMember, ChapterMemberAdmin)
