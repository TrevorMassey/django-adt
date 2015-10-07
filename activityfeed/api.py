from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, ListAPIView

from activityfeed.models import FeedItem, FeedPost
from activityfeed import serializers
from django_adt.pagination import SmallResultsSetPagination


class FeedPostListCreateAPIView(ListCreateAPIView):

    serializer_class = serializers.FeedPostSerializer

    def get_queryset(self):
        qs = FeedPost.objects.all()
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

feed_post_list = FeedPostListCreateAPIView.as_view()

class FeedItemAPIMixin(object):
    serializer_class = serializers.FeedItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        qs = FeedItem.objects.all()

        if not self.request.user.has_perm('activityfeed.soft_delete_feeditem'):
            qs = qs.filter(is_deleted=False)

        qs = qs.prefetch_related(
            )
        qs = qs.select_related(
            'user',
            'user__rank',

            'chapter',
            'chapter__game',

            'feed_post',
            'feed_post__author',
            'feed_post__author__rank',

            'news',
            'news__article',
            'news__article__author',
            'news__article__author__rank',

            'quote',
            'quote__poster',
            'quote__poster__rank',

            'award',
            )

        return qs

class FeedItemListAPIView(FeedItemAPIMixin, ListAPIView):
    pass


class FeedItemRetrieveDestroyAPIView(FeedItemAPIMixin, RetrieveDestroyAPIView):

    def destroy(self, request, *args, **kwargs):

        if not request.user.has_perm('activityfeed.soft_delete_feeditem'):
            raise PermissionDenied()

        self.object = self.get_object()
        self.object.soft_delete(user=self.request.user)
        serializer = self.get_serializer(self.object)
        return Response(serializer.data, status=status.HTTP_200_OK)

feed_item_list = FeedItemListAPIView.as_view()
feed_item_detail = FeedItemRetrieveDestroyAPIView.as_view()
