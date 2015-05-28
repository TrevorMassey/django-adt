from rest_framework import viewsets
from games.models import Game, Chapter
from games.serializers import GameSerializer, ChapterSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()

    serializer_class = GameSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.select_related('game',).all()

    serializer_class = ChapterSerializer
