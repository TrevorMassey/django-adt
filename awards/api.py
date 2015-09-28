from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from awards.models import Award, AwardCategory, AwardRecipient, AwardImage, AwardType
from awards.serializers import AwardSerializer, AwardCategorySerializer, AwardRecipientSerializer, AwardImageSerializer, \
    AwardTypeSerializer, FullAwardSummarySerializer, BasicAwardRecipientSerializer
from users.models import User


class AwardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Award.objects
    serializer_class = AwardSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()


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


class AwardTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = AwardType.objects
    serializer_class = AwardTypeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()


class AwardTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AwardTypeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Award.objects
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs

award_type_list = AwardTypeListCreateAPIView.as_view()
award_type_detail = AwardTypeRetrieveUpdateDestroyAPIView.as_view()


class AwardImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = AwardImage.objects
    serializer_class = AwardImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()


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

    def perform_create(self, serializer):
        serializer.save()


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

    def perform_create(self, serializer):
        award = get_object_or_404(Award, slug=self.kwargs.get('slug'))
        serializer.save(awarder=self.request.user, award=award)


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
    serializer_class = BasicAwardRecipientSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = AwardRecipient.objects
        qs = qs.select_related('award')
        qs = qs.filter(recipient__slug=self.kwargs.get('slug'))
        return qs

    def perform_create(self, serializer):
        user = get_object_or_404(User, slug=self.kwargs.get('slug'))
        serializer.save(awarder=self.request.user, recipient=user)



class UserAwardRecipientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BasicAwardRecipientSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'recipient__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = AwardRecipient.objects
        qs = qs.select_related('award')
        qs = qs.filter(recipient__slug=self.kwargs.get('slug'))
        qs = qs.filter(id=self.kwargs.get('pk'))
        return qs


user_award_list = UserAwardRecipientListCreateAPIView.as_view()
user_award_detail = UserAwardRecipientRetrieveUpdateDestroyAPIView.as_view()


class AwardSummaryListAPIView(generics.ListAPIView):
    queryset = AwardCategory.objects # TODO change to AwardCategories, join on chapters, or do that in a separate request in the frontend

    serializer_class = FullAwardSummarySerializer

    def get_queryset(self):
        qs = AwardCategory.objects.all()
        qs = qs.prefetch_related(

            'awards',
            'awards__award_recipient',
            )
        qs = qs.select_related(
            'awards__award_recipient__recipient',
            'game',
            'awards__image',
            'awards__type',
            'chapter',
            'chapter__game'
            )

        return qs


awards_summary = AwardSummaryListAPIView.as_view()
