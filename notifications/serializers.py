from rest_framework.serializers import ModelSerializer

from users.serializers import BasicUserSerializer, RankSerializer
from games.serializers import ChapterSerializer
from awards.serializers import AwardSerializer

from notifications.models import Notification


class NotificationSerializer(ModelSerializer):

    creator = BasicUserSerializer()

    rank = RankSerializer()
    award = AwardSerializer()
    chapter = ChapterSerializer()

    class Meta:
        model = Notification
        fields = (
            'type',
            'created',

            'user',
            'creator',

            'chapter',
            'rank',
            'award',
        )
