from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from awards.models import Award, AwardCategory, AwardRecipient, AwardImage
from awards.serializers import AwardSerializer, AwardCategorySerializer, AwardRecipientSerializer, AwardImageSerializer, \
    ChapterAwardSummarySerializer
from games.models import Chapter


# TODO urls.py for awardcategory,  everything for award-image

class AwardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Award.objects
    serializer_class = AwardSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AwardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AwardSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Award.objects
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


award_list = AwardListCreateAPIView.as_view()
award_detail = AwardRetrieveUpdateDestroyAPIView.as_view()


class AwardImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = AwardImage.objects
    serializer_class = AwardImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AwardImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AwardImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = AwardImage.objects
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


award_image_list = AwardImageListCreateAPIView.as_view()
award_image_detail = AwardImageRetrieveUpdateDestroyAPIView.as_view()


class AwardCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = AwardCategory.objects
    serializer_class = AwardCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AwardCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AwardCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = AwardCategory.objects
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


award_category_list = AwardCategoryListCreateAPIView.as_view()
award_category_detail = AwardCategoryRetrieveUpdateDestroyAPIView.as_view()


class AwardRecipientListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AwardRecipientSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = AwardRecipient.objects
        qs = qs.filter(award__slug=self.kwargs.get('slug'))
        return qs



class AwardRecipientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AwardRecipientSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'award__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = AwardRecipient.objects
        qs = qs.filter(award__slug=self.kwargs.get('slug'))
        qs = qs.filter(id=self.kwargs.get('pk'))
        return qs


award_recipient_list = AwardRecipientListCreateAPIView.as_view()
award_recipient_detail = AwardRecipientRetrieveUpdateDestroyAPIView.as_view()


class UserAwardRecipientListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AwardRecipientSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = AwardRecipient.objects
        qs = qs.filter(recipient__slug=self.kwargs.get('slug'))
        return qs



class UserAwardRecipientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AwardRecipientSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'recipient__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = AwardRecipient.objects
        qs = qs.filter(recipient__slug=self.kwargs.get('slug'))
        qs = qs.filter(id=self.kwargs.get('pk'))
        return qs


user_award_list = UserAwardRecipientListCreateAPIView.as_view()
user_award_detail = UserAwardRecipientRetrieveUpdateDestroyAPIView.as_view()


class AwardSummaryListAPIView(generics.ListAPIView):
    queryset = Chapter.objects

    serializer_class = ChapterAwardSummarySerializer

    def get_queryset(self):
        qs = Chapter.objects.all()
        qs = qs.prefetch_related(
            'award_categories',
            'award_categories__awards',
            'award_categories__awards__award_recipient',
            )
        qs = qs.select_related(
            'award_categories__awards__award_recipient__recipient',
            'game',
            'award_categories__awards__image',
            'award_categories__awards__type',
            )

        return qs


awards_summary = AwardSummaryListAPIView.as_view()
