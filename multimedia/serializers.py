from rest_framework import serializers
from multimedia.models import Screenshot, Quote
from users.serializers import BasicUserSerializer


class ScreenshotSerializer(serializers.ModelSerializer):
    poster = BasicUserSerializer()

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

    class Meta:
        model = Quote
        fields = (
            'title',
            'body',
            'type',
            'image',

            'poster',
            'involved',
        )
