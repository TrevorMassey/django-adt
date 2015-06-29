from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from dossiers.models import Guild, UserRole, DossierRole, Dossier, Heading, Note, Issue
from dossiers.serializers import GuildSerializer, UserRoleSerializer, DossierRoleSerializer, DossierSerializer, \
    HeadingSerializer, NoteSerializer, IssueSerializer
from users.models import User


class GuildListCreateAPIView(generics.ListCreateAPIView):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class GuildRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guild.objects
    serializer_class = GuildSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Guild.objects
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


guild_list = GuildListCreateAPIView.as_view()
guild_detail = GuildRetrieveUpdateDestroyAPIView.as_view()


class IssueListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'involved__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Issue.objects.prefetch_related('involved').select_related('chapter')
        qs = qs.filter(involved__slug=self.kwargs.get('slug'))
        return qs

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class IssueRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'involved__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Issue.objects.prefetch_related('involved').select_related('chapter')
        qs = qs.filter(involved__slug=self.kwargs.get('slug'))
        return qs


issue_list = IssueListCreateAPIView.as_view()
issue_detail = IssueRetrieveUpdateDestroyAPIView.as_view()


class UserRoleListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserRoleSerializer
    permission_classes = (IsAuthenticated,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = UserRole.objects
        qs = qs.filter(user__slug=self.kwargs.get('slug'))
        return qs

    def perform_create(self, serializer):
        user = get_object_or_404(User, slug=self.kwargs.get('slug'))
        serializer.save(user=user)


class UserRoleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserRoleSerializer
    permission_classes = (IsAuthenticated,)

    lookup_field = 'user__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = UserRole.objects
        qs = qs.filter(user__slug=self.kwargs.get('slug'))
        qs = qs.filter(id=self.kwargs.get('pk'))
        return qs


user_role_list = UserRoleListCreateAPIView.as_view()
user_role_detail = UserRoleRetrieveUpdateDestroyAPIView.as_view()


class DossierRoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = DossierRole.objects.all()
    serializer_class = DossierRoleSerializer
    permission_classes = (IsAuthenticated,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = DossierRole.objects
        qs = qs.filter(dossier__slug=self.kwargs.get('slug'))
        return qs

    def perform_create(self, serializer):
        dossier = get_object_or_404(Dossier, slug=self.kwargs.get('slug'))
        serializer.save(dossier=dossier)


class DossierRoleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DossierRole.objects
    serializer_class = DossierRoleSerializer
    permission_classes = (IsAuthenticated,)

    lookup_field = 'dossier__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = DossierRole.objects
        qs = qs.filter(dossier__slug=self.kwargs.get('slug'))
        qs = qs.filter(id=self.kwargs.get('pk'))
        return qs


dossier_role_list = DossierRoleListCreateAPIView.as_view()
dossier_role_detail = DossierRoleRetrieveUpdateDestroyAPIView.as_view()


class HeadingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Heading.objects.all()
    serializer_class = HeadingSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class HeadingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Heading.objects
    serializer_class = HeadingSerializer
    permission_classes = (IsAuthenticated,)


heading_list = HeadingListCreateAPIView.as_view()
heading_detail = HeadingRetrieveUpdateDestroyAPIView.as_view()


class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Note.objects.select_related('game', 'created_by')
        qs = qs.filter(dossier__slug=self.kwargs.get('slug'))
        return qs

    def perform_create(self, serializer):
        dossier = get_object_or_404(Dossier, slug=self.kwargs.get('slug'))
        serializer.save(created_by=self.request.user, dossier=dossier)


class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    lookup_field = 'dossier__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Note.objects.select_related('game', 'created_by')
        qs = qs.filter(dossier__slug=self.kwargs.get('slug'))
        qs = qs.filter(id=self.kwargs.get('pk'))
        return qs


note_list = NoteListCreateAPIView.as_view()
note_detail = NoteRetrieveUpdateDestroyAPIView.as_view()


class DossierListCreateAPIView(generics.ListCreateAPIView):
    queryset = Dossier.objects.filter(subject_rel=None)
    serializer_class = DossierSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class NonUserDossierRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = DossierSerializer
    permission_classes = (IsAuthenticated,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Dossier.objects.prefetch_related('roles', 'notes')
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


class UserDossierRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = DossierSerializer
    permission_classes = (IsAuthenticated,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Dossier.objects.prefetch_related('roles', 'notes')
        qs = qs.filter(subject_rel__slug=self.kwargs.get('slug'))
        return qs


dossier_list = DossierListCreateAPIView.as_view()
dossier_detail = NonUserDossierRetrieveUpdateAPIView.as_view()
dossier_detail_user = UserDossierRetrieveUpdateAPIView.as_view()
