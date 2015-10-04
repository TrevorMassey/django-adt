from rest_framework import serializers
from accounting.models import DonateCost, DonateAmount, DonateGoal
from users.serializers import BasicUserSerializer


class DonateCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonateCost
        fields = (
            'id',
            'service',
            'amount',
            'created',
        )
        read_only_fields = (
            'id',
            'created',
        )


class DonateAmountSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer(read_only=True)

    class Meta:
        model = DonateAmount
        fields = (
            'id',
            'user',
            'amount',
            'created',
        )
        read_only_fields = (
            'id',
            'user',
            'created',
        )


class DonateGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonateGoal
        fields = (
            'id',
            'amount',
            'created',
            'end',
            'description',
        )
        read_only_fields = (
            'id',
            'created',
        )

