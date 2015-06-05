from rest_framework import serializers
from games.models import Game, Chapter, ChapterMember

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

    class Meta:
        model = ChapterMember
        fields = ('member', 'join_date', 'leave_date',)
