from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from dkp.models import Location, Entity, Item, Section, Event, EventAttendance, EventItem, EventEntity
from dkp.serializers import LocationSerializer, EntitySerializer, ItemSerializer, SectionSerializer, EventSerializer, \
    EventDetailSerializer, EventAttendanceSerializer, EventItemSerializer, EventEntitySerializer


class SectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        qs = Section.objects
        qs = qs.select_related('chapter', 'chapter__game')
        return qs


class SectionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Section.objects
        qs = qs.filter(slug=self.kwargs.get('slug'))
        qs = qs.select_related('chapter', 'chapter__game')
        return qs

section_list = SectionListCreateAPIView.as_view()
section_detail = SectionRetrieveUpdateDestroyAPIView.as_view()


class LocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'section__slug'
    lookup_url_kwarg = 'section_slug'

    def get_queryset(self):
        qs = Location.objects
        qs = qs.filter(section__slug=self.kwargs.get('section_slug'))
        return qs


class LocationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'location_slug'

    def get_queryset(self):
        qs = Location.objects
        qs = qs.filter(section__slug=self.kwargs.get('section_slug'))
        qs = qs.filter(slug=self.kwargs.get('location_slug'))
        return qs


location_list = LocationListCreateAPIView.as_view()
location_detail = LocationRetrieveUpdateDestroyAPIView.as_view()


class EntityListCreateAPIView(generics.ListCreateAPIView):
    queryset = Entity.objects
    serializer_class = EntitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'location_slug'

    def get_queryset(self):
        qs = Entity.objects
        qs = qs.filter(location__section__slug=self.kwargs.get('section_slug'))
        qs = qs.filter(location__slug=self.kwargs.get('location_slug'))
        return qs


class EntityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entity.objects
    serializer_class = EntitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'entity_slug'

    def get_queryset(self):
        qs = Entity.objects
        qs = qs.filter(location__section__slug=self.kwargs.get('section_slug'))
        qs = qs.filter(location__slug=self.kwargs.get('location_slug'))
        qs = qs.filter(slug=self.kwargs.get('entity_slug'))
        return qs


entity_list = EntityListCreateAPIView.as_view()
entity_detail = EntityRetrieveUpdateDestroyAPIView.as_view()


class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Item.objects
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'item_slug'

    def get_queryset(self):
        qs = Item.objects
        qs = qs.filter(entity__location__section__slug=self.kwargs.get('section_slug'))
        qs = qs.filter(entity__location__slug=self.kwargs.get('location_slug'))
        qs = qs.filter(entity__slug=self.kwargs.get('entity_slug'))
        return qs


class ItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'item_slug'

    def get_queryset(self):
        qs = Item.objects
        qs = qs.filter(entity__location__section__slug=self.kwargs.get('section_slug'))
        qs = qs.filter(entity__location__slug=self.kwargs.get('location_slug'))
        qs = qs.filter(entity__slug=self.kwargs.get('entity_slug'))
        qs = qs.filter(slug=self.kwargs.get('item_slug'))
        return qs


item_list = ItemListCreateAPIView.as_view()
item_detail = ItemRetrieveUpdateDestroyAPIView.as_view()


class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'section__slug'
    lookup_url_kwarg = 'section_slug'

    def get_queryset(self):
        qs = Event.objects
        qs = qs.filter(section__slug=self.kwargs.get('section_slug'))
        qs = qs.select_related('location')
        return qs


class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects
    serializer_class = EventDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'event_slug'

    def get_queryset(self):
        qs = Event.objects
        qs = qs.filter(section__slug=self.kwargs.get('section_slug'))
        qs = qs.filter(slug=self.kwargs.get('event_slug'))
        qs = qs.select_related('location')
        qs = qs.prefetch_related('entities', 'awarded_items', 'attendees')
        return qs


event_list = EventListCreateAPIView.as_view()
event_detail = EventRetrieveUpdateDestroyAPIView.as_view()


class EventAttendanceListCreateAPIView(generics.ListCreateAPIView):
    queryset = EventAttendance.objects.all()
    serializer_class = EventAttendanceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        qs = EventAttendance.objects
        qs = qs.filter(event__section__slug=self.kwargs.get('section_slug'))
        qs = qs.filter(event__slug=self.kwargs.get('event_slug'))
        return qs


class EventAttendanceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventAttendance.objects
    serializer_class = EventAttendanceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        qs = EventAttendance.objects
        qs = qs.filter(event__section__slug=self.kwargs.get('section_slug'))
        qs = qs.filter(event__slug=self.kwargs.get('event_slug'))
        qs = qs.filter(id=self.kwargs.get('pk'))
        return qs


eventattendance_list = EventAttendanceListCreateAPIView.as_view()
eventattendance_detail = EventAttendanceRetrieveUpdateDestroyAPIView.as_view()


class EventItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = EventItem.objects.all()
    serializer_class = EventItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        qs = EventItem.objects
        qs = qs.filter(event__section__slug=self.kwargs.get('section_slug'))
        qs = qs.filter(event__slug=self.kwargs.get('event_slug'))
        qs = qs.select_related('item')
        return qs


class EventItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventItem.objects
    serializer_class = EventItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        qs = EventItem.objects
        qs = qs.filter(event__section__slug=self.kwargs.get('section_slug'))
        qs = qs.filter(event__slug=self.kwargs.get('event_slug'))
        qs = qs.filter(id=self.kwargs.get('pk'))
        qs = qs.select_related('item')
        return qs


eventitem_list = EventItemListCreateAPIView.as_view()
eventitem_detail = EventItemRetrieveUpdateDestroyAPIView.as_view()


class EventEntityListCreateAPIView(generics.ListCreateAPIView):
    queryset = EventEntity.objects.all()
    serializer_class = EventEntitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        qs = EventEntity.objects
        qs = qs.filter(event__section__slug=self.kwargs.get('section_slug'))
        qs = qs.filter(event__slug=self.kwargs.get('event_slug'))
        qs = qs.select_related('entity')
        return qs


class EventEntityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventEntity.objects
    serializer_class = EventEntitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        qs = EventEntity.objects
        qs = qs.filter(event__section__slug=self.kwargs.get('section_slug'))
        qs = qs.filter(event__slug=self.kwargs.get('event_slug'))
        qs = qs.filter(id=self.kwargs.get('pk'))
        qs = qs.select_related('entity')
        return qs


evententity_list = EventEntityListCreateAPIView.as_view()
evententity_detail = EventEntityRetrieveUpdateDestroyAPIView.as_view()
