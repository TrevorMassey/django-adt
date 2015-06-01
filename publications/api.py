from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from publications.models import Article, News, Codex
from publications.serializers import ArticleSerializer, NewsSerializer, CodexSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()

    serializer_class = ArticleSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()

    serializer_class = NewsSerializer

class CodexListAPIView(generics.ListAPIView):
    queryset = Codex.objects.root_nodes()
    serializer_class = CodexSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CodexRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Codex.objects
    serializer_class = CodexSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


codex_list = CodexListAPIView.as_view()
codex_detail = CodexRetrieveUpdateDestroyAPIView.as_view()