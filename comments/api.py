from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # TODO make this work for any model without having to explicitly write news__slug etc. for each one

    # lookup_field = 'slug'
    # lookup_url_kwarg = 'slug'
    #
    # def get_queryset(self):
    #     qs = Comment.objects
    #     qs = qs.filter(slug=self.kwargs.get('slug'))
    #     return qs


comment_list = CommentListAPIView.as_view()
comment_detail = CommentRetrieveUpdateDestroyAPIView.as_view()
