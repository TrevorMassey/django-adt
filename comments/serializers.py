from rest_framework import serializers
from comments.models import Comment
from users.serializers import BasicUserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer()
    deleted_by = BasicUserSerializer()

    class Meta:
        model = Comment
        fields = ('body',
                  'created',
                  'public',

                  'is_deleted',
                  'deleted_by',
                  'deleted_time',

                  'user',
                  )
