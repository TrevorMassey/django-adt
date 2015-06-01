from django.contrib import admin
from publications.models import Article, News, Codex

from mptt.admin import MPTTModelAdmin


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('article',)


class CodexMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Article, ArticleAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Codex, CodexMPTTModelAdmin)
