from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_adt.pagination import StandardResultsSetPagination
from games.models import Game, Chapter, ChapterMember, ChapterDivision
from games.serializers import GameSerializer, ChapterSerializer, ChapterMemberSerializer, ChapterDivisionSerializer


class GameListCreateAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()


class GameRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Game.objects
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


game_list = GameListCreateAPIView.as_view()
game_detail = GameRetrieveUpdateDestroyAPIView.as_view()


class ChapterListCreateAPIView(generics.ListCreateAPIView):
    queryset = Chapter.objects.select_related('game',)
    serializer_class = ChapterSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()


class ChapterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.select_related('game',)
    serializer_class = ChapterSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


chapter_list = ChapterListCreateAPIView.as_view()
chapter_detail = ChapterRetrieveUpdateDestroyAPIView.as_view()


class ChapterMemberListAPIView(generics.ListAPIView):
    serializer_class = ChapterMemberSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        qs = ChapterMember.objects.select_related('member', 'chapter', 'division')
        qs = qs.filter(chapter=self.kwargs.get('pk'))
        return qs

    def perform_create(self, serializer):
        serializer.save()


class ChapterMemberRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChapterMemberSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'member__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = ChapterMember.objects.select_related('member', 'chapter', 'division')
        qs = qs.filter(chapter=self.kwargs.get('pk'))
        qs = qs.filter(member__slug=self.kwargs.get('slug'))
        return qs


chapter_member_list = ChapterMemberListAPIView.as_view()
chapter_member_detail = ChapterMemberRetrieveUpdateDestroyAPIView.as_view()


class ChapterDivisionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ChapterDivisionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        qs = ChapterDivision.objects.root_nodes()
        qs = qs.prefetch_related('members', 'members__member')
        qs = qs.filter(chapter=self.kwargs.get('pk'))
        return qs

    def perform_create(self, serializer):
        serializer.save()


class ChapterDivisionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChapterDivisionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = ChapterDivision.objects.prefetch_related('members', 'members__member')
        qs = qs.filter(chapter=self.kwargs.get('pk'))
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


chapter_division_list = ChapterDivisionListCreateAPIView.as_view()
chapter_division_detail = ChapterDivisionRetrieveUpdateDestroyAPIView.as_view()
