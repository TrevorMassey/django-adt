from rest_framework import viewsets
from users.models import Rank
from users.serializers import RankSerializer


class RankViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()

    serializer_class = RankSerializer
