from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from games.models import Game, Chapter, ChapterMember, ChapterDivision, ChapterRole
from games.serializers import GameSerializer, ChapterSerializer, ChapterMemberSerializer, ChapterDivisionSerializer, \
    ChapterRoleSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()

    serializer_class = GameSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.select_related('game',).all()

    serializer_class = ChapterSerializer


class ChapterMemberViewSet(viewsets.ModelViewSet):
    queryset = ChapterMember.objects.select_related('member',).all()

    serializer_class = ChapterMemberSerializer


class ChapterDivisionListAPIView(generics.ListAPIView):
    queryset = ChapterDivision.objects.root_nodes()
    serializer_class = ChapterDivisionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ChapterDivisionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChapterDivision.objects
    serializer_class = ChapterDivisionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ChapterRoleViewSet(viewsets.ModelViewSet):
    queryset = ChapterRole.objects.select_related('member',).all()

    serializer_class = ChapterRoleSerializer

chapter_division_list = ChapterDivisionListAPIView.as_view()
chapter_division_detail = ChapterDivisionRetrieveUpdateDestroyAPIView.as_view()
