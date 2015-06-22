from rest_framework import serializers
from polls.models import Poll, Item, Vote
from users.serializers import BasicUserSerializer


class VoteSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer(read_only=True)

    class Meta:
        model = Vote
        fields = ('id', 'created', 'poll', 'item', 'user',)
        read_only_fields = ('id', 'created', 'user',)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'answer', 'order', 'poll', 'vote_count',)
        read_only_fields = ('id', 'vote_count',)


class PollSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'title', 'slug', 'created', 'items',)
        read_only_fields = ('id', 'slug', 'created', 'items',)
