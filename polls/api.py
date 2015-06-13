from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from polls.models import Poll, Item, Vote
from polls.serializers import PollSerializer, ItemSerializer, VoteSerializer


class PollListCreateAPIView(generics.ListCreateAPIView):
    queryset = Poll.objects.prefetch_related('items')
    serializer_class = PollSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PollRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Poll.objects.prefetch_related('items')
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


poll_list = PollListCreateAPIView.as_view()
poll_detail = PollRetrieveUpdateDestroyAPIView.as_view()


class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Item.objects
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'poll__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Item.objects
        qs = qs.filter(poll__slug=self.kwargs.get('slug'))
        return qs


class ItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'poll__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Item.objects
        qs = qs.filter(id=self.kwargs.get('pk'))
        qs = qs.filter(poll__slug=self.kwargs.get('slug'))
        return qs


item_list = ItemListCreateAPIView.as_view()
item_detail = ItemRetrieveUpdateDestroyAPIView.as_view()


class VoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vote.objects
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'poll__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Vote.objects
        qs = qs.filter(poll__slug=self.kwargs.get('slug'))
        return qs


class VoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'poll__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Vote.objects
        qs = qs.filter(poll__slug=self.kwargs.get('slug'))
        qs = qs.filter(id=self.kwargs.get('pk'))
        return qs


vote_list = VoteListCreateAPIView.as_view()
vote_detail = VoteRetrieveUpdateDestroyAPIView.as_view()