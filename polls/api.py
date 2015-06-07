from rest_framework import viewsets
from polls.models import Poll, Item, Vote
from polls.serializers import PollSerializer, ItemSerializer, VoteSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()

    serializer_class = PollSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()

    serializer_class = ItemSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()

    serializer_class = VoteSerializer
