from rest_framework.serializers import ModelSerializer

from activityfeed.models import FeedItem, FeedPost

from users.serializers import BasicUserSerializer, RankSerializer
from games.serializers import ChapterSerializer
from publications.serializers import NewsSerializer
from awards.serializers import AwardSerializer


class FeedPostSerializer(ModelSerializer):
    author = BasicUserSerializer()

    class Meta:
        model = FeedPost
        fields = (
            'author',
            'created',
            'body',
        )

class FeedItemSerializer(ModelSerializer):
    user = BasicUserSerializer()

    feed_post = FeedPostSerializer()
    rank = RankSerializer()
    award = AwardSerializer()
    news = NewsSerializer()
    chapter = ChapterSerializer()

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
