from rest_framework import serializers
from games.serializers import ChapterSerializer
from multimedia.models import Screenshot, Quote
from users.serializers import BasicUserSerializer


class ScreenshotSerializer(serializers.ModelSerializer):
    poster = BasicUserSerializer()
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


class QuoteSerializer(serializers.ModelSerializer):
    poster = BasicUserSerializer()
    involved = BasicUserSerializer(many=True)

    class Meta:
        model = Quote
        fields = (
            'title',
            'slug',
            'body',
            'type',
            'image',

            'poster',
            'involved',
        )
