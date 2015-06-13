from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from multimedia.models import Screenshot, Quote
from multimedia.serializers import ScreenshotSerializer, QuoteSerializer


class ScreenshotListAPIView(generics.ListAPIView):
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ScreenshotRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screenshot.objects
    serializer_class = ScreenshotSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Screenshot.objects.prefetch_related('involved')
        qs = qs.select_related('chapter')
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


class QuoteListAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class QuoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects
    serializer_class = QuoteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Quote.objects.prefetch_related('involved')
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


screenshot_list = ScreenshotListAPIView.as_view()
screenshot_detail = ScreenshotRetrieveUpdateDestroyAPIView.as_view()
quote_list = QuoteListAPIView.as_view()
quote_detail = QuoteRetrieveUpdateDestroyAPIView.as_view()
