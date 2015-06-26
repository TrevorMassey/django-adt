from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from dkp.models import Location
from dkp.serializers import LocationSerializer


class LocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LocationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Location.objects
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


location_list = LocationListCreateAPIView.as_view()
location_detail = LocationRetrieveUpdateDestroyAPIView.as_view()
