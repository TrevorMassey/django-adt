from rest_framework import serializers
from games.models import Game, Chapter, ChapterMember, ChapterRole, ChapterDivision
from users.serializers import BasicUserSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'slug',)


class ChapterSerializer(serializers.ModelSerializer):
    game = GameSerializer()

    class Meta:
        model = Chapter
        fields = ('id', 'game', 'open_date', 'launch_date', 'close_date',)


class ChapterMemberSerializer(serializers.ModelSerializer):
    member = BasicUserSerializer()

    class Meta:
        model = ChapterMember
        fields = ('member', 'join_date', 'leave_date',)


class ChapterRoleSerializer(serializers.ModelSerializer):
    member = BasicUserSerializer()

    class Meta:
        model = ChapterRole
        fields = ('member', 'division', 'role',)


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ChapterDivisionSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    members = ChapterRoleSerializer(many=True)

    class Meta:
        model = ChapterDivision
        fields = ('title', 'order', 'parent', 'members', 'children')

    def get_children(self, obj):
        return ChapterDivisionSerializer(obj.get_children(), many=True).data
