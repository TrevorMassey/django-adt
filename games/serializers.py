from rest_framework import serializers
from games.models import Game, Chapter, ChapterMember, ChapterDivision
from users.serializers import BasicUserSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('title', 'slug',)


class ChapterSerializer(serializers.ModelSerializer):
    game = GameSerializer()

    class Meta:
        model = Chapter
        fields = ('id', 'game', 'open_date', 'launch_date', 'close_date',)


class BasicChapterDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterDivision
        fields = ('title', 'slug',)


class ChapterMemberSerializer(serializers.ModelSerializer):
    member = BasicUserSerializer()
    division = BasicChapterDivisionSerializer()

    class Meta:
        model = ChapterMember
        fields = ('member', 'join_date', 'leave_date', 'role', 'division',)


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ChapterDivisionSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    members = ChapterMemberSerializer(many=True)

    class Meta:
        model = ChapterDivision
        fields = ('title', 'slug', 'order', 'parent', 'members', 'children')

    def get_children(self, obj):
        return ChapterDivisionSerializer(obj.get_children(), many=True).data
