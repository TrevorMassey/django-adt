from django.contrib import admin
from publications.models import Article, News


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('article',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(News, NewsAdmin)
