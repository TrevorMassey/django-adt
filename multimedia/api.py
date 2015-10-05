from django.db.models import F
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from comments.api import BaseCommentListCreateAPIView, BaseCommentRetrieveUpdateAPIView
from multimedia.models import Screenshot, Quote
from multimedia.serializers import ScreenshotSerializer, QuoteSerializer


class ScreenshotListCreateAPIView(generics.ListCreateAPIView):
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class ScreenshotRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Screenshot.objects.prefetch_related('involved')
        qs = qs.select_related('chapter')
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.queryset.filter(id=instance.id).update(views=F('views') + 1)
        return Response(serializer.data)



class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class QuoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Quote.objects.prefetch_related('involved')
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs



screenshot_list = ScreenshotListCreateAPIView.as_view()
screenshot_detail = ScreenshotRetrieveUpdateDestroyAPIView.as_view()
quote_list = QuoteListCreateAPIView.as_view()
quote_detail = QuoteRetrieveUpdateDestroyAPIView.as_view()


class ScreenshotCommentAPIMixin(object):
    parent_queryset = Screenshot.objects.all()

class ScreenshotCommentListCreateAPIView(ScreenshotCommentAPIMixin, BaseCommentListCreateAPIView):
    pass

class ScreenshotCommentRetrieveUpdateAPIView(ScreenshotCommentAPIMixin, BaseCommentRetrieveUpdateAPIView):
    pass

screenshot_comment_list = ScreenshotCommentListCreateAPIView.as_view()
screenshot_comment_detail = ScreenshotCommentRetrieveUpdateAPIView.as_view()


class QuoteCommentAPIMixin(object):
    parent_queryset = Quote.objects.all()

class QuoteCommentListCreateAPIView(QuoteCommentAPIMixin, BaseCommentListCreateAPIView):
    pass

class QuoteCommentRetrieveUpdateAPIView(QuoteCommentAPIMixin, BaseCommentRetrieveUpdateAPIView):
    pass

quote_comment_list = QuoteCommentListCreateAPIView.as_view()
quote_comment_detail = QuoteCommentRetrieveUpdateAPIView.as_view()
