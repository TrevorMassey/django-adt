from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from users.models import Rank, User
from users.serializers import RankSerializer, UserRegistrationSerializer, UserProfileSerializer


class RankListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rank.objects
    serializer_class = RankSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RankRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RankSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Rank.objects
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


rank_list = RankListCreateAPIView.as_view()
rank_detail = RankRetrieveUpdateDestroyAPIView.as_view()


class UserRegistrationAPIView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny, )

user_registration = UserRegistrationAPIView.as_view()


class UserProfileAPIView(generics.RetrieveUpdateAPIView):

    queryset = User.objects.none()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user

user_profile = UserProfileAPIView.as_view()
