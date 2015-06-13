from django.core.urlresolvers import reverse
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from django_extensions.db.fields import AutoSlugField


class Codex(MPTTModel):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    order = models.PositiveIntegerField(default=0)

    # Relationship Fields
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    article = models.OneToOneField('publications.Article', blank=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'codex'
        verbose_name_plural = 'codex'

    class MPTTMeta:
        order_insertion_by = 'order'

    def __unicode__(self):
        return u'%s' % self.slug


class Article(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    body = models.TextField()

    # Relationship Fields
    author = models.ForeignKey('users.User', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.title


class News(models.Model):

    # TODO this needs reimplementing better.  Cannot set title that is different from article, slug difficult.
    # should investigate using multi-table inheritance?

    # Fields
    image = models.ImageField(upload_to='images/news/', blank=True, null=True)

    # Relationship Fields
    article = models.OneToOneField('publications.Article', blank=True, null=True)
    chapter = models.ForeignKey('games.Chapter', blank=True, null=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __unicode__(self):
        return u'%s' % self.article