from rest_framework import serializers
from dossiers.models import Guild, UserRole, DossierRole, Dossier, Heading, Note
from games.serializers import GameSerializer


class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = ('title', 'slug', 'created',)


class UserRoleSerializer(serializers.ModelSerializer):
    guild = GuildSerializer()
    game = GameSerializer()

    class Meta:
        model = UserRole
        fields = ('role', 'created', 'duration', 'guild', 'game',)


class DossierRoleSerializer(serializers.ModelSerializer):
    guild = GuildSerializer()
    game = GameSerializer()

    class Meta:
        model = DossierRole
        fields = ('role', 'created', 'duration', 'guild', 'game',)


class DossierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dossier
        fields = ('subject', 'slug', 'subject_rel', 'created', 'created_by',)


class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = ('title', 'created', 'created_by',)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('body', 'created', 'created_by',)
