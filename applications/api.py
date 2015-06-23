from applications.models import Application
from comments.api import BaseCommentListCreateAPIView, BaseCommentRetrieveUpdateAPIView


class ApplicationCommentAPIMixin(object):
    parent_queryset = Application.objects.all()

class ApplicationCommentListCreateAPIView(ApplicationCommentAPIMixin, BaseCommentListCreateAPIView):
    pass

class ApplicationCommentRetrieveUpdateAPIView(ApplicationCommentAPIMixin, BaseCommentRetrieveUpdateAPIView):
    pass

application_comment_list = ApplicationCommentListCreateAPIView.as_view()
application_comment_detail = ApplicationCommentRetrieveUpdateAPIView.as_view()
