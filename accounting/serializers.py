from rest_framework import serializers
from accounting.models import DonateCost, DonateAmount


class DonateCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonateCost
        fields = ('service', 'amount', 'created', 'last_updated',)


class DonateAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonateAmount
        fields = ('user', 'amount', 'created',)


class DonateGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonateAmount
        fields = ('amount', 'created', 'end', 'description',)
