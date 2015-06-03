from rest_framework import serializers
from users.models import Rank, User


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = ('title', 'order', 'image', 'description', 'color')


class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = (
            'display_name',
            'email',
            'password',
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):

    permissions = serializers.SerializerMethodField('get_user_permissions')

    class Meta:
        model = User
        fields = (
            'display_name',
            'email',
            'permissions',
        )

    def get_user_permissions(self, obj):
        return [perm for perm in obj.get_all_permissions()]


class BasicUserSerializer(serializers.ModelSerializer):

    rank = RankSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'display_name',
            'avatar',
            'rank',
            'id',
        )