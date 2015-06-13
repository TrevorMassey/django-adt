from rest_framework import serializers
from dossiers.models import Guild, UserRole, DossierRole, Dossier, Heading, Note
from games.serializers import GameSerializer
from users.serializers import BasicUserSerializer


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


class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = ('id', 'title', 'created', 'created_by',)


class NoteSerializer(serializers.ModelSerializer):
    created_by = BasicUserSerializer()
    game = GameSerializer()

    class Meta:
        model = Note
        fields = ('id', 'body', 'created', 'created_by', 'game',)


class DossierSerializer(serializers.ModelSerializer):
    roles = DossierRoleSerializer(many=True)
    notes = NoteSerializer(many=True)

    class Meta:
        model = Dossier
        fields = ('subject', 'slug', 'subject_rel', 'created', 'created_by', 'roles', 'notes')
