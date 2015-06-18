from rest_framework import serializers
from games.serializers import ChapterSerializer
from multimedia.models import Screenshot, Quote
from users.serializers import BasicUserSerializer


class ScreenshotSerializer(serializers.ModelSerializer):
    poster = BasicUserSerializer(read_only=True)
    chapter = ChapterSerializer()
    involved = BasicUserSerializer(many=True)

    class Meta:
        model = Screenshot
        fields = (
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
            'slug',
            'views',
            'created',
            'poster',
        )


class QuoteSerializer(serializers.ModelSerializer):
    poster = BasicUserSerializer(read_only=True)
    involved = BasicUserSerializer(many=True)

    class Meta:
        model = Quote
        fields = (
            'title',
            'slug',
            'body',
            'created',
            'type',
            'image',
            'poster',
            'involved',
        )
        read_only_fields = (
            'slug',
            'created',
            'poster',
        )
