from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from notifications import serializers
from notifications.models import Notification


class NotificationListAPIView(ListAPIView):
    serializer_class = serializers.NotificationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(user=user)

notification_list = NotificationListAPIView.as_view()
