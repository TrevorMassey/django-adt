from django.core.urlresolvers import reverse
from django.db import models
from django_extensions.db.fields import AutoSlugField


class User(models.Model):

    # Fields
    display_name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    email = models.CharField(max_length=255)
    signed_in = models.BooleanField()
    last_active = models.DateTimeField(auto_now=True, editable=False)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField()

    # Relationship Fields
    rank = models.ForeignKey('users.Rank',)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

class Rank(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True)
    number = models.IntegerField()
    image = models.FilePathField()
    description = models.TextField()
    color = models.CharField(max_length=6)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug

