from rest_framework import serializers
from awards.models import Award, AwardCategory, AwardRecipient, AwardImage, AwardType
from games.models import Chapter
from games.serializers import ChapterSerializer, GameSerializer
from users.serializers import BasicUserSerializer


class AwardImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AwardImage
        fields = ('id', 'title', 'slug', 'image',)


class AwardTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AwardType
        fields = ('id', 'name', 'slug',)
        read_only_fields = ('id', 'slug',)


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'title', 'slug', 'level_limit', 'order', 'description', 'category', 'image', 'type',)
        read_only_fields = ('id', 'slug',)


class AwardFullSerializer(serializers.ModelSerializer):
    image = AwardImageSerializer(read_only=True)
    type = AwardTypeSerializer(read_only=True)

    class Meta:
        model = Award
        fields = ('id', 'title', 'slug', 'level_limit', 'order', 'description', 'category', 'image', 'type',)
        read_only_fields = ('id', 'slug',)


class AwardCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AwardCategory
        fields = ('id', 'title', 'slug', 'order', 'chapter',)
        read_only_fields = ('id', 'slug',)


class BasicAwardRecipientSerializer(serializers.ModelSerializer):
    award = AwardSerializer(read_only=True)

    class Meta:
        model = AwardRecipient
        fields = ('id', 'recipient', 'award', 'reason',)
        read_only_fields = ('id',)


class AwardRecipientSerializer(serializers.ModelSerializer):
    recipient = BasicUserSerializer()
    award = AwardSerializer()

    class Meta:
        model = AwardRecipient
        fields = ('id', 'recipient', 'award', 'reason',)
        read_only_fields = ('id',)


class AwardSummaryRecipientSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(source='recipient.display_name',)

    class Meta:
        model = AwardRecipient
        fields = ('id', 'recipient', 'display_name', 'reason',)



class AwardSummarySerializer(serializers.ModelSerializer):
    #recipients = AwardRecipientSerializer(source='award_recipient', many=True)
    image = serializers.SerializerMethodField(method_name='get_image_url')
    type = serializers.CharField(source='type.name')

    class Meta:
        model = Award
        fields = (
            'id',
            'title',
            'slug',
            'level_limit',
            'order',
            'description',
            #'recipients',
            'image',
            'type',
            )

    def get_image_url(self, obj):
        return obj.image.image.url


class AwardCategorySummarySerializer(serializers.ModelSerializer):
    awards = AwardSummarySerializer(many=True)

    class Meta:
        model = AwardCategory
        fields = (
            'id',
            'title',
            'slug',
            'order',
            'awards',
        )



class FullAwardSummarySerializer(serializers.ModelSerializer):
    award_categories = AwardCategorySummarySerializer(many=True)
    game = GameSerializer(read_only=True)

    class Meta:
        model = Chapter
        fields = (
            'id',
            'game',
            'award_categories',
        )
