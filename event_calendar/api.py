import logging
from django.utils import timezone
import pytz

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from schedule.models import Event
from schedule.periods import Period
from event_calendar import serializers

logger = logging.getLogger(__name__)

class EventListCreateAPIView(ListCreateAPIView):

    serializer_class = serializers.EventOccurrenceSerializer
    permission_classes = (IsAuthenticated,)
    default_window_days = 7

    def get_window_days(self):
        return self.request.data.get('days', self.default_window_days)

    def get_period_window(self):
        start = self.request.data.get('start')
        end = self.request.data.get('end')

        if start and end:
            pass

        elif start:
            end = start + timezone.timedelta(days=self.get_window_days())

        elif not start:
            start = timezone.now()
            end = start + timezone.timedelta(days=self.get_window_days())

        return start, end

    def get_queryset(self):
        event_qs = Event.objects.all()
        start, end = self.get_period_window()
        period = Period(event_qs, start, end)
        occurrences = period.get_occurrences()
        return occurrences

    def get_serializer_context(self):
        tz_string = self.request.query_params.get('timezone')
        logger.info(self.request.query_params)
        tz = pytz.timezone(tz_string)

        context = {
            'timezone': tz,
        }
        return context

event_list = EventListCreateAPIView.as_view()