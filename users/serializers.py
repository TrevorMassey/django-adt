from rest_framework import serializers
from users.models import Rank


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = ('title', 'number', 'image', 'description', 'color')
