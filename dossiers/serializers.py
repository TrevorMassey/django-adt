from rest_framework import serializers
from dossiers.models import Guild, UserRole, DossierRole, Dossier, Heading, Note, Issue
from games.serializers import GameSerializer, ChapterSerializer
from users.serializers import BasicUserSerializer


class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = ('id', 'title', 'slug', 'created',)
        read_only_fields = ('id', 'slug', 'created',)


class IssueSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer()
    involved = BasicUserSerializer(many=True)

    class Meta:
        model = Issue
        fields = ('id', 'description', 'created', 'created_by', 'chapter', 'involved',)
        read_only_fields = ('id', 'created', 'created_by',)


class UserRoleSerializer(serializers.ModelSerializer):
    guild = GuildSerializer()
    game = GameSerializer()

    class Meta:
        model = UserRole
        fields = ('id', 'role', 'created', 'duration', 'guild', 'game',)
        read_only_fields = ('id', 'created', 'duration',)


class DossierRoleSerializer(serializers.ModelSerializer):
    guild = GuildSerializer()
    game = GameSerializer()

    class Meta:
        model = DossierRole
        fields = ('id', 'role', 'created', 'duration', 'guild', 'game',)
        read_only_fields = ('id', 'created', 'duration',)


class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = ('id', 'title', 'created', 'created_by',)
        read_only_fields = ('id', 'created', 'created_by',)


class NoteSerializer(serializers.ModelSerializer):
    created_by = BasicUserSerializer()
    game = GameSerializer()

    class Meta:
        model = Note
        fields = ('id', 'body', 'created', 'created_by', 'game',)
        read_only_fields = ('id', 'created', 'created_by',)


class DossierSerializer(serializers.ModelSerializer):
    roles = DossierRoleSerializer(many=True)
    notes = NoteSerializer(many=True)

    class Meta:
        model = Dossier
        fields = ('subject', 'slug', 'subject_rel', 'created', 'created_by', 'roles', 'notes')
        read_only_fields = ('slug', 'created', 'created_by', 'roles', 'notes')
