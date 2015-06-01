from rest_framework import serializers
from awards.models import Award, AwardCategory, AwardRecipient, AwardImage
from games.models import Chapter
from games.serializers import ChapterSerializer, GameSerializer


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'title', 'slug',)


class AwardCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AwardCategory
        fields = ('chapter', 'title',)


class AwardRecipientSerializer(serializers.ModelSerializer):
    #recipient = UserSerializer()
    award = AwardSerializer()

    class Meta:
        model = AwardRecipient
        fields = ('recipient', 'award', 'reason',)


class AwardImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AwardImage
        fields = ('title', 'image',)


class AwardSummaryRecipientSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(source='recipient.display_name',)

    class Meta:
        model = AwardRecipient
        fields = ('recipient', 'display_name', 'reason',)


class AwardSummarySerializer(serializers.ModelSerializer):
    recipients = AwardRecipientSerializer(source='award_recipient', many=True)
    image = serializers.SerializerMethodField(method_name='get_image_url')
    type = serializers.CharField(source='type.name')

    class Meta:
        model = Award
        fields = ('id', 'title', 'slug', 'level_limit', 'order', 'description', 'recipients', 'image', 'type',)

    def get_image_url(self, obj):
        return obj.image.image.url


class AwardCategorySummarySerializer(serializers.ModelSerializer):
    awards = AwardSummarySerializer(many=True)

    class Meta:
        model = AwardCategory
        fields = (
            'title',
            'slug',
            'awards',
        )


class ChapterAwardSummarySerializer(ChapterSerializer):
    categories = AwardCategorySummarySerializer(source='award_categories', many=True)

    game = GameSerializer()

    class Meta:
        model = Chapter
        fields = (
            'id',
            'game',
            'open_date',
            'launch_date',
            'close_date',
            'categories',
        )
