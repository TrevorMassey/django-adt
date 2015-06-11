from rest_framework import viewsets
from dossiers.models import Guild, UserRole, DossierRole, Dossier, Heading, Note
from dossiers.serializers import GuildSerializer, UserRoleSerializer, DossierRoleSerializer, DossierSerializer, \
    HeadingSerializer, NoteSerializer


class GuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()

    serializer_class = GuildSerializer


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()

    serializer_class = UserRoleSerializer


class DossierRoleViewSet(viewsets.ModelViewSet):
    queryset = DossierRole.objects.all()

    serializer_class = DossierRoleSerializer


class DossierViewSet(viewsets.ModelViewSet):
    queryset = Dossier.objects.all()

    serializer_class = DossierSerializer


class HeadingViewSet(viewsets.ModelViewSet):
    queryset = Heading.objects.all()

    serializer_class = HeadingSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()

    serializer_class = NoteSerializer


# TODO:  Clean these up with select_related and more specific
# views (dossier includes headings and notes for that dossier)
