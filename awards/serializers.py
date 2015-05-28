from rest_framework import serializers
from awards.models import Award, AwardCategory, AwardRecipient, AwardImage


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
