from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from accounting.models import DonateCost, DonateAmount, DonateGoal
from accounting.serializers import DonateCostSerializer, DonateAmountSerializer, DonateGoalSerializer


class DonateAmountListCreateAPIView(generics.ListCreateAPIView):
    queryset = DonateAmount.objects
    serializer_class = DonateAmountSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DonateAmountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonateAmount.objects
    serializer_class = DonateAmountSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


donate_list = DonateAmountListCreateAPIView.as_view()
donate_detail = DonateAmountRetrieveUpdateDestroyAPIView.as_view()


class DonateCostListCreateAPIView(generics.ListCreateAPIView):
    queryset = DonateCost.objects
    serializer_class = DonateCostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



class DonateCostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonateCost.objects
    serializer_class = DonateCostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


cost_list = DonateCostListCreateAPIView.as_view()
cost_detail = DonateCostRetrieveUpdateDestroyAPIView.as_view()


class DonateGoalListCreateAPIView(generics.ListCreateAPIView):
    queryset = DonateGoal.objects
    serializer_class = DonateGoalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class DonateGoalRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonateGoal.objects
    serializer_class = DonateGoalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


goal_list = DonateGoalListCreateAPIView.as_view()
goal_detail = DonateGoalRetrieveUpdateAPIView.as_view()

