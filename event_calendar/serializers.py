from django.utils import timezone
from rest_framework import serializers
from schedule.models import Rule


class EventOccurrenceSerializer(serializers.Serializer):

    event_id = serializers.IntegerField(read_only=True)
    calendar = serializers.IntegerField(source='event.calendar_id')
    creator = serializers.IntegerField(source='event.creator')
    title = serializers.CharField()
    description = serializers.CharField()

    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()

    original_start = serializers.DateTimeField()
    original_end = serializers.DateTimeField()
    cancelled = serializers.BooleanField()

    end_recurring_period = serializers.DateTimeField(source='event.end_recurring_period')
    rule_id = serializers.PrimaryKeyRelatedField(queryset=Rule.objects.all(), source='event.rule_id')
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()

    def get_tz(self):
        return self.context['timezone']

    def get_start(self, obj):
        tz = self.get_tz()
        return obj.start.astimezone(tz)

    def get_end(self, obj):
        tz = self.get_tz()
        return obj.end.astimezone(tz)

    def get_original_start(self, obj):
        tz = self.get_tz()
        return obj.original_start.astimezone(tz)

    def get_original_end(self, obj):
        tz = self.get_tz()
        return obj.original_end.astimezone(tz)
