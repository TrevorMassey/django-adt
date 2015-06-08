from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone


class Comment(models.Model):
    # Fields
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey('users.User', blank=True, null=True, related_name='+')
    deleted_time = models.DateTimeField(blank=True, null=True)

    # Relationships
    user = models.ForeignKey('users.User')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return u'%s' % (self.user,)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        permissions = (
            ('soft_delete_comment', 'Can soft delete comment'),
        )

    def soft_delete(self, user):
        self.deleted_by = user
        self.is_deleted = True
        self.deleted_time = timezone.now()
        self.save()
