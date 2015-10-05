from rest_framework import serializers
from games.models import Game, Chapter, ChapterMember, ChapterDivision
from users.models import User
from users.serializers import BasicUserSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'slug',)
        read_only_fields = ('id', 'slug',)


class ChapterSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    game_id = serializers.PrimaryKeyRelatedField(source='game', queryset=Game.objects.all())

    class Meta:
        model = Chapter
        fields = (
            'id',
            'game',
            'game_id',
            'open_date',
            'launch_date',
            'close_date',
            'divisions',
        )
        read_only_fields = (
            'id',
            'game',
        )


class BasicChapterDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterDivision
        fields = ('id', 'title', 'slug',)
        read_only_fields = ('id', 'slug',)


class ChapterMemberSerializer(serializers.ModelSerializer):
    member = BasicUserSerializer()
    member_id = serializers.PrimaryKeyRelatedField(source='member', queryset=User.objects.all())
    division = BasicChapterDivisionSerializer()
    division_id = serializers.PrimaryKeyRelatedField(source='division', queryset=ChapterDivision.objects.all())

    class Meta:
        model = ChapterMember
        fields = (
            'id',
            'member',
            'member_id',
            'join_date',
            'leave_date',
            'role',
            'division',
            'division_id',
        )
        read_only_fields = (
            'id',
            'member',
            'join_date',
            'leave_date',
            'division',
        )


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ChapterDivisionSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)
    members = ChapterMemberSerializer(many=True)
    members_ids = serializers.PrimaryKeyRelatedField(source='members', queryset=User.objects.all(), many=True)

    class Meta:
        model = ChapterDivision
        fields = (
            'id',
            'title',
            'slug',
            'order',
            'chapter',
            'parent',
            'members',
            'members_ids',
            'children'
        )
        read_only_fields = (
            'id',
            'slug',
            'children'
        )

    def get_children(self, obj):
        return ChapterDivisionSerializer(obj.get_children(), many=True).data
