from rest_framework import viewsets
from publications.models import Article, News
from publications.serializers import ArticleSerializer, NewsSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()

    serializer_class = ArticleSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()

    serializer_class = NewsSerializer
