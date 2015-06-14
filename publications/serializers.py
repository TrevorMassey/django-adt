from rest_framework import serializers
from comments.models import Comment
from comments.serializers import CommentSerializer
from publications.models import Article, News, Codex
from games.serializers import ChapterSerializer
from users.serializers import BasicUserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    author = BasicUserSerializer()

    class Meta:
        model = Article
        fields = ('title', 'created', 'last_updated', 'body', 'author')


class CommentRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        if isinstance(value, Comment):
            serializer = CommentSerializer(value)
        else:
            raise Exception('Unexpected type of comment')

        return serializer.data

class NewsSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    chapter = ChapterSerializer()
    comments = CommentRelatedField()

    class Meta:
        model = News
        fields = ('title', 'slug', 'image', 'article', 'chapter', 'comments',)

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
