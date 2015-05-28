from django.contrib import admin
from games.models import Game, Chapter

class GameAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('game', 'open_date', 'launch_date', 'close_date')

admin.site.register(Game, GameAdmin)
admin.site.register(Chapter, ChapterAdmin)
