from rest_framework import serializers
from publications.models import Article, News
from games.serializers import ChapterSerializer


class ArticleSerializer(serializers.ModelSerializer):
    #author = UserSerializer
    class Meta:
        model = Article
        fields = ('title', 'created', 'last_updated', 'body', 'body_clean', 'author')


class NewsSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    chapter = ChapterSerializer()

    class Meta:
        model = News
        fields = ('article', 'chapter',)
