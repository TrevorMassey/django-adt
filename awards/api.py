from rest_framework import viewsets
from awards.models import Award, AwardCategory, AwardRecipient, AwardImage
from awards.serializers import AwardSerializer, AwardCategorySerializer, AwardRecipientSerializer, AwardImageSerializer


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
