from rest_framework import serializers
from games.models import Chapter
from publications.models import Article, News, Codex
from games.serializers import ChapterSerializer
from users.serializers import BasicUserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    author = BasicUserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'created', 'last_updated', 'body', 'author')
        read_only_fields = ('id', 'slug', 'created', 'last_updated', 'author')


class NewsSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    chapter = ChapterSerializer(read_only=True)

    article_id = serializers.PrimaryKeyRelatedField(source='article', queryset=Article.objects.filter(news__isnull=True))
    chapter_id = serializers.PrimaryKeyRelatedField(source='chapter', queryset=Chapter.objects.all())

    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'slug',
            'image',
            'article',
            'chapter',
            'article_id',
            'chapter_id',
        )
        read_only_fields = ('id', 'slug',)

    def create(self, validated_data):
        news = News(**validated_data)
        news.save()
        return news

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
        read_only_fields = (
            'id',
            'slug',
            'created',
            'last_updated',
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
        read_only_fields = (
            'id',
            'slug',
            'created',
            'last_updated',
        )

    def get_children(self, obj):
        return NoChildrenCodexSerializer(obj.get_children().select_related('article'), many=True).data
