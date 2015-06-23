from rest_framework.serializers import ModelSerializer

from activityfeed.models import FeedItem, FeedPost

from users.serializers import BasicUserSerializer, RankSerializer
from games.serializers import ChapterSerializer
from publications.serializers import NewsSerializer
from awards.serializers import AwardSerializer


class FeedPostSerializer(ModelSerializer):
    author = BasicUserSerializer(read_only=True)

    class Meta:
        model = FeedPost
        fields = (
            'id',
            'author',
            'created',
            'body',
        )
        read_only_fields = (
            'id',
            'author',
            'created',
        )

class FeedItemSerializer(ModelSerializer):
    user = BasicUserSerializer(read_only=True)

    feed_post = FeedPostSerializer(read_only=True)
    rank = RankSerializer(read_only=True)
    award = AwardSerializer(read_only=True)
    news = NewsSerializer(read_only=True)
    chapter = ChapterSerializer(read_only=True)

    class Meta:
        model = FeedItem
        fields = (
            'id',
            'user',
            'type',
            'created',
            'public',
            'is_deleted',
            'deleted_by',
            'deleted_time',

            'chapter',
            'news',
            'rank',
            'feed_post',
            'award',
        )
        read_only_fields = (
            'id',
            'user',
            'type',
            'created',
            'public',
            'is_deleted',
            'deleted_by',
            'deleted_time',

            'chapter',
            'news',
            'rank',
            'feed_post',
            'award',
        )
