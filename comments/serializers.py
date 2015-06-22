import logging

from rest_framework import serializers
from comments.models import Comment
from users.serializers import BasicUserSerializer

logger = logging.getLogger(__name__)

class CommentSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer(read_only=True)
    deleted_by = BasicUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'body',
            'user',
            'created',
            'public',
            'is_deleted',
            'deleted_by',
            'deleted_time',
        )
        read_only_fields = (
            'id',
            'created',
            'public',
            'is_deleted',
            'deleted_by',
            'deleted_time',
        )
