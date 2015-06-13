from rest_framework import serializers
from polls.models import Poll, Item, Vote
from users.serializers import BasicUserSerializer


class VoteSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer()

    class Meta:
        model = Vote
        fields = ('created', 'poll', 'item', 'user',)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('answer', 'order', 'poll', 'vote_count',)


class PollSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('title', 'slug', 'created', 'items',)
