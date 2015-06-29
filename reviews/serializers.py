from rest_framework import serializers
from reviews.models import Review, Vote
from users.models import User
from users.serializers import BasicUserSerializer


class VoteSerializer(serializers.ModelSerializer):
    created_by = BasicUserSerializer(read_only=True)

    class Meta:
        model = Vote
        fields = (
            'id',
            'vote',
            'created',
            'created_by',
        )
        read_only_fields = (
            'id',
            'created',
            'created_by',
        )


class ReviewSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())
    created_by = BasicUserSerializer(read_only=True)
    votes = VoteSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'user_id',
            'description',
            'created',
            'created_by',
            'votes',
        )
        read_only_fields = (
            'id',
            'created',
            'created_by',
            'votes',
        )
