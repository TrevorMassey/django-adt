from rest_framework import serializers
from awards.models import Award, AwardCategory, AwardRecipient, AwardImage, AwardType
from games.models import Chapter
from games.serializers import ChapterSerializer, GameSerializer
from users.serializers import BasicUserSerializer


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'title', 'slug', 'level_limit', 'order', 'description', 'category', 'image', 'type',)
        read_only_fields = ('id', 'slug',)


class AwardTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AwardType
        fields = ('id', 'name', 'slug',)
        read_only_fields = ('id', 'slug',)

class AwardCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AwardCategory
        fields = ('id', 'title', 'slug', 'order', 'chapter',)
        read_only_fields = ('id', 'slug',)


class AwardRecipientSerializer(serializers.ModelSerializer):
    recipient = BasicUserSerializer()
    award = AwardSerializer()

    class Meta:
        model = AwardRecipient
        fields = ('id', 'recipient', 'award', 'reason',)
        read_only_fields = ('id',)


class AwardImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AwardImage
        fields = ('id', 'title', 'slug', 'image',)


class AwardSummaryRecipientSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(source='recipient.display_name',)

    class Meta:
        model = AwardRecipient
        fields = ('id', 'recipient', 'display_name', 'reason',)


class AwardSummarySerializer(serializers.ModelSerializer):
    recipients = AwardRecipientSerializer(source='award_recipient', many=True)
    image = serializers.SerializerMethodField(method_name='get_image_url')
    type = serializers.CharField(source='type.name')

    class Meta:
        model = Award
        fields = ('id', 'title', 'slug', 'level_limit', 'order', 'description', 'recipients', 'image', 'type',)

    def get_image_url(self, obj):
        return obj.image.image.url




class FullAwardSummarySerializer(serializers.ModelSerializer):
    awards = AwardSummarySerializer(many=True)

    class Meta:
        model = AwardCategory
        fields = ('id', 'title', 'slug', 'order', 'chapter', 'awards',)
