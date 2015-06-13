from rest_framework import serializers
from publications.models import Article, News, Codex
from games.serializers import ChapterSerializer
from users.serializers import BasicUserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    author = BasicUserSerializer()

    class Meta:
        model = Article
        fields = ('title', 'created', 'last_updated', 'body', 'author')


class NewsSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    chapter = ChapterSerializer()

    class Meta:
        model = News
        fields = ('article', 'chapter',)

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class NoChildrenCodexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Codex
        fields = (
            'id',
            'title',
            'slug',
            'created',
            'last_updated',
            'order',
            'parent',
            'article',
        )



class CodexSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Codex
        fields = (
            'id',
            'title',
            'slug',
            'created',
            'last_updated',
            'order',
            'parent',
            'children',
            'article',
        )

    def get_children(self, obj):
        return NoChildrenCodexSerializer(obj.get_children().select_related('article'), many=True).data
