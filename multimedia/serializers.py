import logging

from rest_framework import serializers
from games.serializers import ChapterSerializer
from multimedia.models import Screenshot, Quote
from users.models import User
from users.serializers import BasicUserSerializer

logger = logging.getLogger(__name__)


class ScreenshotSerializer(serializers.ModelSerializer):
    poster = BasicUserSerializer(read_only=True)
    chapter = ChapterSerializer()
    involved = BasicUserSerializer(many=True)

    class Meta:
        model = Screenshot
        fields = (
            'id',
            'title',
            'slug',
            'views',
            'created',
            'image',
            'poster',
            'chapter',
            'involved',
        )
        read_only_fields = (
            'id',
            'slug',
            'views',
            'created',
            'poster',
        )


class QuoteSerializer(serializers.ModelSerializer):
    poster = BasicUserSerializer(read_only=True)
    involved = BasicUserSerializer(many=True, read_only=True)
    involved_ids = serializers.PrimaryKeyRelatedField(source='involved', queryset=User.objects.all(), many=True)

    class Meta:
        model = Quote
        fields = (
            'id',
            'title',
            'slug',
            'body',
            'created',
            'type',
            'image',
            'poster',
            'involved',
            'involved_ids',
        )
        read_only_fields = (
            'id',
            'slug',
            'created',
            'poster',
            'involved',
        )

    def create(self, validated_data):

        involved = validated_data.pop('involved')
        quote = Quote(**validated_data)
        quote.save()

        quote.involved = involved

        return quote
