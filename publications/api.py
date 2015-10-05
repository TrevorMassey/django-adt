from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from comments.api import BaseCommentListCreateAPIView, BaseCommentRetrieveUpdateAPIView
from django_adt.pagination import NewsResultsSetPagination

from publications.models import Article, News, Codex
from publications.serializers import ArticleSerializer, NewsSerializer, CodexSerializer

class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Article.objects
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


article_list = ArticleListCreateAPIView.as_view()
article_detail = ArticleRetrieveUpdateDestroyAPIView.as_view()


class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    pagination_class = NewsResultsSetPagination
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        qs = News.objects.all()
        qs = qs.prefetch_related(
            )
        qs = qs.select_related(
            'article',
            'article__author',
            'article__author__rank',
            'chapter',
            'chapter__game',
            )

        return qs


class NewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = News.objects
        qs = qs.filter(slug=self.kwargs.get('slug'))
        return qs


news_list = NewsListCreateAPIView.as_view()
news_detail = NewsRetrieveUpdateDestroyAPIView.as_view()


class CodexListAPIView(generics.ListAPIView):
    queryset = Codex.objects.root_nodes()
    serializer_class = CodexSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CodexRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Codex.objects.all()
    serializer_class = CodexSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


codex_list = CodexListAPIView.as_view()
codex_detail = CodexRetrieveUpdateDestroyAPIView.as_view()


class NewsCommentAPIMixin(object):
    parent_queryset = Article.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

class NewsCommentListCreateAPIView(NewsCommentAPIMixin, BaseCommentListCreateAPIView):
    pass

class NewsCommentRetrieveUpdateAPIView(NewsCommentAPIMixin, BaseCommentRetrieveUpdateAPIView):
    pass

news_comment_list = NewsCommentListCreateAPIView.as_view()
news_comment_detail = NewsCommentRetrieveUpdateAPIView.as_view()


class CodexCommentAPIMixin(object):
    parent_queryset = Article.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

class CodexCommentListCreateAPIView(CodexCommentAPIMixin, BaseCommentListCreateAPIView):
    pass

class CodexCommentRetrieveUpdateAPIView(CodexCommentAPIMixin, BaseCommentRetrieveUpdateAPIView):
    pass

codex_comment_list = CodexCommentListCreateAPIView.as_view()
codex_comment_detail = CodexCommentRetrieveUpdateAPIView.as_view()


class ArticleCommentAPIMixin(object):
    parent_queryset = Article.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ArticleCommentListCreateAPIView(ArticleCommentAPIMixin, BaseCommentListCreateAPIView):
    pass

class ArticleCommentRetrieveUpdateAPIView(ArticleCommentAPIMixin, BaseCommentRetrieveUpdateAPIView):
    pass

article_comment_list = ArticleCommentListCreateAPIView.as_view()
article_comment_detail = ArticleCommentRetrieveUpdateAPIView.as_view()
