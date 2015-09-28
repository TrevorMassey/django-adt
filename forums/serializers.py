from rest_framework import serializers
from forums.models import Forum, Topic, Post

__author__ = 'Alex'


class ForumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Forum
        fields = (
            'id',
            'slug',
            'title',
            'slug',
            'description',
            'type',
            'link_url',
            'topic_count',
            'post_count',
            'last_post_on',
            'last_thread',
            'last_thread_slug',
            'last_poster',
        )


class TopicSerializer(serializers.ModelSerializer):

    body = serializers.CharField(max_length=10000, write_only=True)

    class Meta:
        model = Topic
        fields = (
            'id',
            'forum',
            'body',
            'label',
            'title',
            'slug',
            'created',
            'replies',
            'views',
            'is_announcement',
            'is_pinned',
            'is_poll',
            'is_locked',
            'first_post',
            'starter',
            'last_post_on',
            'last_post',
            'is_deleted',
            'deleted_by',
            'deleted_time',
        )

    def create(self, validated_data):
        # create topic using manager with validated data
        topic = Topic.objects.create_topic()

        return topic

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'forum',
            'thread',
            'poster',
            'created',
            'body',
            'posted',
            'updated',
            'edits',
            'last_editor',
            'is_deleted',
            'deleted_by',
            'deleted_time',
        )