from rest_framework import viewsets, generics
from awards.models import Award, AwardCategory, AwardRecipient, AwardImage
from awards.serializers import AwardSerializer, AwardCategorySerializer, AwardRecipientSerializer, AwardImageSerializer, \
    ChapterAwardSummarySerializer
from games.models import Chapter


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()

    serializer_class = AwardSerializer


class AwardCategoryViewSet(viewsets.ModelViewSet):
    queryset = AwardCategory.objects.all()

    serializer_class = AwardCategorySerializer


class AwardRecipientViewSet(viewsets.ModelViewSet):
    queryset = AwardRecipient.objects.all()

    serializer_class = AwardRecipientSerializer


class AwardImageViewSet(viewsets.ModelViewSet):
    queryset = AwardImage.objects.all()

    serializer_class = AwardImageSerializer


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
