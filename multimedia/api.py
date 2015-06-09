from rest_framework import viewsets
from multimedia.models import Screenshot, Quote
from multimedia.serializers import ScreenshotSerializer, QuoteSerializer


class ScreenshotViewSet(viewsets.ModelViewSet):
    queryset = Screenshot.objects.all()

    serializer_class = ScreenshotSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()

    serializer_class = QuoteSerializer
