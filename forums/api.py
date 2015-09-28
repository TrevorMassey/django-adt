import logging

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from forums import serializers
from forums.models import Forum, Topic, Post

logger = logging.getLogger(__name__)


class ForumAPIMixin(object):
    forum_queryset = Forum.objects.all()
    serializer_class = serializers.ForumSerializer
    forum_lookup_url_kwarg = 'forum_slug'
    forum_lookup_field = 'slug'

    forum = None

    def get_forum_queryset(self):
        return self.forum_queryset

    def get_forum(self):

        if self.forum is None:
            queryset = self.get_forum_queryset()
            lookup_url_kwarg = self.forum_lookup_url_kwarg
            filter_kwargs = {self.forum_lookup_field: self.kwargs[lookup_url_kwarg]}
            forum = get_object_or_404(queryset, **filter_kwargs)
            self.forum = forum

        return self.forum

    def get_queryset(self):
        return self.get_forum_queryset()

class ForumListCreateAPIView(ForumAPIMixin, generics.ListCreateAPIView):
    pass

class ForumRetrieveUpdateDestroyAPIView(ForumAPIMixin, generics.RetrieveUpdateDestroyAPIView):
    def get_object(self):
        return self.get_forum()

forum_list = ForumListCreateAPIView.as_view()
forum_detail = ForumRetrieveUpdateDestroyAPIView.as_view()


class TopicAPIMixin(ForumAPIMixin):
    topic_queryset = Topic.objects.all()
    serializer_class = serializers.TopicSerializer
    topic_lookup_url_kwarg = 'topic_slug'
    topic_lookup_field = 'slug'
    topic = None

    def get_topic_queryset(self):
        self.forum = self.get_forum()
        queryset = self.topic_queryset
        queryset = queryset.filter(forum=self.forum)
        return queryset

    def get_topic(self):
        if self.topic is None:
            queryset = self.get_topic_queryset()
            filter_kwargs = {self.topic_lookup_field: self.kwargs[self.topic_lookup_url_kwarg]}
            topic = get_object_or_404(queryset, **filter_kwargs)
            self.topic = topic
        return self.topic

    def get_queryset(self):
        return self.get_topic_queryset()


class TopicListCreateAPIView(TopicAPIMixin, generics.ListCreateAPIView):
    pass

class TopicRetrieveUpdateDestroyAPIView(TopicAPIMixin, generics.ListCreateAPIView):
    def get_object(self):
        return self.get_topic()

topic_list = TopicListCreateAPIView.as_view()
topic_detail = TopicRetrieveUpdateDestroyAPIView.as_view()


class PostAPIMixin(TopicAPIMixin):
    serializer_class = serializers.PostSerializer
    post_queryset = Post.objects.all()
    post_lookup_url_kwarg = 'post_pk'
    post_lookup_field = 'id'

    def get_post_queryset(self):
        self.topic = self.get_topic()
        queryset = self.post_queryset
        queryset = queryset.filter(thread=self.topic)
        return queryset

    def get_post(self):
        queryset = self.get_post_queryset()
        filter_kwargs = {self.post_lookup_field: self.kwargs[self.post_lookup_url_kwarg]}
        topic = get_object_or_404(queryset, **filter_kwargs)
        return topic

    def get_queryset(self):
        return self.get_post_queryset()


class PostListCreateAPIView(PostAPIMixin, generics.ListCreateAPIView):
    pass

class PostRetrieveUpdateDestroyAPIView(PostAPIMixin, generics.RetrieveUpdateDestroyAPIView):
    def get_object(self):
        return self.get_post()

post_list = PostListCreateAPIView.as_view()
post_detail = PostRetrieveUpdateDestroyAPIView.as_view()
