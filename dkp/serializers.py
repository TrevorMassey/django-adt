from rest_framework import serializers
from dkp.models import Location, Event, ResourceContrib, Resource, Bonus, Section, Item, Entity, EventAttendance, \
    EventItem, EventEntity


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'dkp',
            'game',
        )
        read_only_fields = (
            'id',
            'slug',
            'game',
        )

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = (
            'id',
            'title',
            'slug',
            'dkp',
            'location',
        )
        read_only_fields = (
            'id',
            'slug',
            'location',
        )

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'slug',
            'entity',
        )
        read_only_fields = (
            'id',
            'slug',
            'entity',
        )


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = (
            'id',
            'title',
            'slug',
            'created',
            'closed',
            'chapter',
        )
        read_only_fields = (
            'id',
            'slug',
            'chapter',
        )

class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = (
            'id',
            'dkp',
            'user',
        )
        read_only_fields = (
            'id',
            'user',
        )

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = (
            'id',
            'title',
            'slug',
            'dkp',
            'section'
        )
        read_only_fields = (
            'id',
            'slug',
            'section'
        )

class ResourceContribSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceContrib
        fields = (
            'id',
            'amount',
            'created',
            'created_by',
            'resource',
            'user',
        )
        read_only_fields = (
            'id',
            'created',
            'created_by',
            'resource',
        )

class EventSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'slug',
            'created',
            'created_by',
            'event_leader',
            'section',
            'location',
            'location_id',
            'started',
            'stopped',
            'scheduled',
        )
        read_only_fields = (
            'id',
            'slug',
            'created',
            'created_by',
            'section',
            'location',
        )

class EventAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendance
        fields = (
            'id',
            'event',
            'user',
            'started',
            'stopped',
            'standby',

        )
        read_only_fields = (
            'id',
            'event',
        )

class EventItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventItem
        fields = (
            'id',
            'dkp',
            'created',
            'attendee',
            'item',

        )
        read_only_fields = (
            'id',
            'created',
            'attendee',
        )

class EventEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventEntity
        fields = (
            'id',
            'event',
            'entity',
            'created',

        )
        read_only_fields = (
            'id',
            'event'
            'created',
        )
