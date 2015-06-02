from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import Rank, User
from users.serializers import RankSerializer, UserRegistrationSerializer, UserProfileSerializer


class RankViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()

    serializer_class = RankSerializer


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
