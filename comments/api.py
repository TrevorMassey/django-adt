from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from comments.models import Comment
from comments.serializers import CommentSerializer


class NewsCommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    lookup_field = 'content_object__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Comment.objects
        qs = qs.filter(content_object__slug=self.kwargs.get('slug'))
        if not self.request.user.has_perm('comments.soft_delete_comment'):
            qs = qs.filter(is_deleted=False)
        return qs


class NewsCommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # TODO make this work for any model without having to explicitly write news__slug etc. for each one

    lookup_field = 'object_id__slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Comment.objects
        qs = qs.filter(slug=self.kwargs.get('slug'))
        qs = qs.filter(id=self.kwargs.get('pk'))

        if not self.request.user.has_perm('comments.soft_delete_comment'):
          qs = qs.filter(is_deleted=False)

        return qs

    def destroy(self, request, *args, **kwargs):

        if not request.user.has_perm('comments.soft_delete_comment'):
            raise PermissionDenied()

        self.object = self.get_object()
        self.object.soft_delete(user=self.request.user)
        serializer = self.get_serializer(self.object)
        return Response(serializer.data, status=status.HTTP_200_OK)


news_comment_list = NewsCommentListAPIView.as_view()
news_comment_detail = NewsCommentRetrieveUpdateDestroyAPIView.as_view()
