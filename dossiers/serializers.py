from rest_framework import serializers
from dossiers.models import Guild, Role


class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = ('title',)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('role',)
