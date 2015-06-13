from rest_framework import viewsets
from accounting.models import DonateCost, DonateAmount, DonateGoal
from accounting.serializers import DonateCostSerializer, DonateAmountSerializer, DonateGoalSerializer


class DonateCostViewSet(viewsets.ModelViewSet):
    queryset = DonateCost.objects.all()

    serializer_class = DonateCostSerializer


class DonateAmountViewSet(viewsets.ModelViewSet):
    queryset = DonateAmount.objects.all()

    serializer_class = DonateAmountSerializer


class DonateGoalViewSet(viewsets.ModelViewSet):
    queryset = DonateGoal.objects.all()

    serializer_class = DonateGoalSerializer
