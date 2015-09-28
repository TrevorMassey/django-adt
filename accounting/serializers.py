from rest_framework import serializers
from accounting.models import DonateCost, DonateAmount, DonateGoal
from users.serializers import BasicUserSerializer


class DonateCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonateCost
        fields = ('service', 'amount', 'created', 'last_updated',)


class DonateAmountSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer(read_only=True)

    class Meta:
        model = DonateAmount
        fields = ('user', 'amount', 'created',)


class DonateGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonateGoal
        fields = ('amount', 'created', 'end', 'description',)
