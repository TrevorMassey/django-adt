from django.contrib.contenttypes.models import ContentType
from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from comments.models import Comment
from comments.serializers import CommentSerializer

import logging

logger = logging.getLogger(__name__)

class CommentAPIMixin(object):
    serializer_class = CommentSerializer
    parent_queryset = None
    queryset = Comment.objects.select_related('user', 'deleted_by')
    parent_url_kwarg = 'slug'
    parent_lookup_field = 'slug'

    def get_parent_queryset(self):
        """
        Ensures a parent model exists for this API View
        """
        assert self.parent_queryset is not None, (
            "'%s' should include a `parent_queryset` attribute, "
            "or override the `get_parent_queryset()` method."
            % self.__class__.__name__
        )
        parent_queryset = self.parent_queryset
        if isinstance(parent_queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = parent_queryset.all()
        return parent_queryset

    def get_content_type_for_parent(self):
        """
        Fetch the content type for the parent model
        """
        content_type = ContentType.objects.get_for_model(self.get_parent_queryset().model)

        return content_type

    def get_parent_object(self):
        """
        Fetches the parent object by its lookup parameters
        """

        filters = {self.parent_lookup_field: self.kwargs.get(self.parent_url_kwarg)}

        parent_object = get_object_or_404(self.get_parent_queryset(), **filters)

        return parent_object

    def get_queryset(self):
        # This runs twice for some unknown jmerlin shit
        content_type = self.get_content_type_for_parent()
        parent = self.get_parent_object()

        queryset = super(CommentAPIMixin, self).get_queryset()

        queryset = queryset.filter(content_type=content_type, object_id=parent.id)

        if not self.request.user.has_perm('comments.soft_delete_comment'):
            queryset = queryset.filter(is_deleted=False)

        return queryset

class BaseCommentListCreateAPIView(CommentAPIMixin, generics.ListCreateAPIView):

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, content_object=self.get_parent_object())


class BaseCommentRetrieveUpdateAPIView(CommentAPIMixin, generics.RetrieveUpdateDestroyAPIView):

    def perform_destroy(self, instance):
        """
        Soft Deletes a comment if not yet deleted.  If comment is already soft deleted and the requesting user is
        allowed, perform hard delete
        """

        if instance.is_deleted:
            if not self.request.user.has_perm('comments.delete_comment'):
                raise PermissionDenied

            instance.delete()

        else:
            if not self.request.user.has_perm('comments.soft_delete_comment'):
                raise PermissionDenied

            instance.soft_delete(user=self.request.user)

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        parent = self.get_parent_object()
        content_type = self.get_content_type_for_parent()

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {
            self.lookup_field: self.kwargs[lookup_url_kwarg],
            'content_type': content_type,
            'object_id': parent.id,
        }

        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
