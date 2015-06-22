from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from games.models import Game, Chapter, ChapterMember, ChapterDivision

class GameAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('game', 'open_date', 'launch_date', 'close_date',)


class ChapterMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'join_date', 'leave_date',)


class ChapterDivisionMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Game, GameAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(ChapterMember, ChapterMemberAdmin)
admin.site.register(ChapterDivision, ChapterDivisionMPTTModelAdmin)
