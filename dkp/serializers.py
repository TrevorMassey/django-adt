from rest_framework import serializers
from dkp.models import Location, Event, ResourceContrib, Resource, Bonus, Section, Item, Entity, EventAttendance, \
    EventItem, EventEntity
from games.models import Chapter
from games.serializers import ChapterSerializer
from users.models import User
from users.serializers import BasicUserSerializer


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'dkp',
            'section',
        )
        read_only_fields = (
            'id',
            'slug',
            'section',
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
    chapter = ChapterSerializer(read_only=True)
    chapter_id = serializers.PrimaryKeyRelatedField(source='chapter', queryset=Chapter.objects.all())

    class Meta:
        model = Section
        fields = (
            'id',
            'title',
            'slug',
            'created',
            'closed',
            'chapter',
            'chapter_id',
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
    created_by = BasicUserSerializer(read_only=True)
    event_leader = BasicUserSerializer(read_only=True)
    event_leader_id = serializers.PrimaryKeyRelatedField(source='event_leader', queryset=User.objects.all())
    location_id = serializers.PrimaryKeyRelatedField(source='location', queryset=Location.objects.all())

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'slug',
            'created',
            'created_by',
            'dkp',
            'event_leader',
            'event_leader_id',
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
            'event_leader'
            'dkp',
            'section',
            'location',
        )

class EventAttendanceSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())

    class Meta:
        model = EventAttendance
        fields = (
            'id',
            'event',
            'user',
            'user_id',
            'started',
            'stopped',
            'standby',

        )
        read_only_fields = (
            'id',
            'event',
        )

class EventItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(source='item', queryset=Item.objects.all())
    user = BasicUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())

    class Meta:
        model = EventItem
        fields = (
            'id',
            'dkp',
            'created',
            'event',
            'item',
            'item_id',
            'user',
            'user_id',

        )
        read_only_fields = (
            'id',
            'created',
            'event',
            'item',
            'user',
        )

class EventEntitySerializer(serializers.ModelSerializer):
    entity = EntitySerializer(read_only=True)
    entity_id = serializers.PrimaryKeyRelatedField(source='entity', queryset=Entity.objects.all())

    class Meta:
        model = EventEntity
        fields = (
            'id',
            'dkp',
            'event',
            'entity',
            'entity_id',
            'created',

        )
        read_only_fields = (
            'id',
            'event'
            'created',
            'entity',
        )


class EventDetailSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    created_by = BasicUserSerializer(read_only=True)
    event_leader = BasicUserSerializer(read_only=True)
    event_leader_id = serializers.PrimaryKeyRelatedField(source='event_leader', queryset=User.objects.all())
    location_id = serializers.PrimaryKeyRelatedField(source='location', queryset=Location.objects.all())
    entities = EventEntitySerializer(read_only=True, many=True)
    items = EventItemSerializer(read_only=True, many=True)
    attendees = EventAttendanceSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'slug',
            'created',
            'created_by',
            'dkp',
            'event_leader',
            'event_leader_id',
            'section',
            'location',
            'location_id',
            'started',
            'stopped',
            'scheduled',
            'entities',
            'items',
            'attendees',
        )
        read_only_fields = (
            'id',
            'slug',
            'created',
            'created_by',
            'event_leader'
            'dkp',
            'section',
            'location',
        )
