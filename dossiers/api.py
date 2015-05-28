from rest_framework import viewsets
from dossiers.models import Guild, Role
from dossiers.serializers import GuildSerializer, RoleSerializer


class GuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()

    serializer_class = GuildSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()

    serializer_class = RoleSerializer
