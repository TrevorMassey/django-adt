from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.models import Review, Vote
from reviews.serializers import ReviewSerializer, VoteSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects
    queryset = queryset.prefetch_related(
        'votes',
        'votes__created_by',
        'votes__created_by__rank',
    )
    queryset = queryset.select_related(
        'created_by',
        'created_by__rank',
        'user',
        'user__rank',
    )
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = Review.objects
        qs = qs.prefetch_related(
            'votes',
            'votes__created_by',
            'votes__created_by__rank',
        )
        qs = qs.select_related(
            'created_by',
            'created_by__rank',
            'user',
            'user__rank',
        )
        qs = qs.filter(pk=self.kwargs.get('pk'))
        return qs


review_list = ReviewListCreateAPIView.as_view()
review_detail = ReviewRetrieveUpdateDestroyAPIView.as_view()


class VoteListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = Vote.objects
        qs = qs.select_related('created_by', 'created_by__rank')
        qs = qs.filter(review__id=self.kwargs.get('pk'))
        return qs

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class VoteRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)

    lookup_field = 'id'
    lookup_url_kwarg = 'vote_pk'

    def get_queryset(self):
        qs = Vote.objects
        qs = qs.select_related('created_by', 'created_by__rank')
        qs = qs.filter(review__id=self.kwargs.get('pk'))
        qs = qs.filter(id=self.kwargs.get('vote_pk'))
        return qs


vote_list = VoteListCreateAPIView.as_view()
vote_detail = VoteRetrieveUpdateAPIView.as_view()
