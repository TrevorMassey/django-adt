from rest_framework import serializers
from dossiers.models import Guild, UserRole, DossierRole, Dossier, Heading, Note, Issue
from games.models import Chapter, Game
from games.serializers import GameSerializer, ChapterSerializer
from users.models import User
from users.serializers import BasicUserSerializer


class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = ('id', 'title', 'slug', 'created',)
        read_only_fields = ('id', 'slug', 'created',)


class IssueSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)
    chapter_id = serializers.PrimaryKeyRelatedField(source='chapter', queryset=Chapter.objects.all())
    involved = BasicUserSerializer(many=True, read_only=True)
    involved_ids = serializers.PrimaryKeyRelatedField(source='involved', queryset=User.objects.all(), many=True)

    class Meta:
        model = Issue
        fields = (
            'id',
            'description',
            'created',
            'created_by',
            'chapter',
            'chapter_id',
            'involved',
            'involved_ids',
        )
        read_only_fields = (
            'id',
            'created',
            'created_by',
            'chapter',
            'involved',
        )


class UserRoleSerializer(serializers.ModelSerializer):
    guild = GuildSerializer(read_only=True)
    guild_id = serializers.PrimaryKeyRelatedField(source='guild', queryset=Guild.objects.all())
    game = GameSerializer(read_only=True)
    game_id = serializers.PrimaryKeyRelatedField(source='game', queryset=Game.objects.all())

    class Meta:
        model = UserRole
        fields = (
            'id',
            'role',
            'created',
            'duration',
            'guild',
            'guild_id',
            'game',
            'game_id',
        )
        read_only_fields = (
            'id',
            'created',
            'duration',
            'guild',
            'game',
        )


class DossierRoleSerializer(serializers.ModelSerializer):
    guild = GuildSerializer(read_only=True)
    guild_id = serializers.PrimaryKeyRelatedField(source='guild', queryset=Guild.objects.all())
    game = GameSerializer(read_only=True)
    game_id = serializers.PrimaryKeyRelatedField(source='game', queryset=Game.objects.all())

    class Meta:
        model = DossierRole
        fields = (
            'id',
            'role',
            'created',
            'duration',
            'guild',
            'guild_id',
            'game',
            'game_id',
        )
        read_only_fields = (
            'id',
            'created',
            'duration',
            'guild',
            'game',
        )


class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = ('id', 'title', 'created', 'created_by',)
        read_only_fields = ('id', 'created', 'created_by',)


class NoteSerializer(serializers.ModelSerializer):
    created_by = BasicUserSerializer(read_only=True)
    game = GameSerializer(read_only=True)
    game_id = serializers.PrimaryKeyRelatedField(source='game', queryset=Game.objects.all())

    class Meta:
        model = Note
        fields = (
            'id',
            'body',
            'created',
            'created_by',
            'game',
            'game_id',
        )
        read_only_fields = (
            'id',
            'created',
            'created_by',
            'game',
        )


class DossierSerializer(serializers.ModelSerializer):
    roles = DossierRoleSerializer(many=True, read_only=True)
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Dossier
        fields = (
            'id',
            'subject',
            'slug',
            'subject_rel',
            'created',
            'created_by',
            'roles',
            'notes'
        )
        read_only_fields = (
            'id',
            'slug',
            'created',
            'created_by',
            'roles',
            'notes'
        )
