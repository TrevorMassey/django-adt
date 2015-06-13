from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, ListAPIView

from activityfeed.models import FeedItem, FeedPost
from activityfeed import serializers


# TODO @Gromph I don't think this needs to be a List, just create
# Should make a second class that lists feed_items for a specific user perhaps?
class FeedPostListCreateAPIView(ListCreateAPIView):

    serializer_class = serializers.FeedPostSerializer

    def get_queryset(self):
        qs = FeedPost.objects.all()
        return qs

feed_post_list = FeedPostListCreateAPIView.as_view()

class FeedItemAPIMixin(object):
    serializer_class = serializers.FeedItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        qs = FeedItem.objects.all()

        if not self.request.user.has_perm('activityfeed.soft_delete_feeditem'):
            qs = qs.filter(is_deleted=False)

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
