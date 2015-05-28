from rest_framework import viewsets
from accounting.models import DonateCost, DonateAmount
from accounting.serializers import DonateCostSerializer, DonateAmountSerializer


class DonateCostViewSet(viewsets.ModelViewSet):
    queryset = DonateCost.objects.all()

    serializer_class = DonateCostSerializer


class DonateAmountViewSet(viewsets.ModelViewSet):
    queryset = DonateAmount.objects.all()

    serializer_class = DonateAmountSerializer
