from rest_framework import serializers
from polls.models import Poll, Item, Vote
from users.serializers import BasicUserSerializer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('title', 'created', 'vote_count',)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('answer', 'order', 'poll', 'vote_count',)


class VoteSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer()

    class Meta:
        model = Vote
        fields = ('created', 'poll', 'item', 'user',)
