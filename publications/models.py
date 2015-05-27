from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django_extensions.db.fields import AutoSlugField


class Codex(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    is_article = models.BooleanField()
    order = models.IntegerField()

    # Relationship Fields
    parent = models.OneToOneField('publications.Codex',)
    article = models.OneToOneField('publications.Article',)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug


class Article(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    body = models.TextField()
    body_clean = models.TextField()

    # Relationship Fields
    author = models.ForeignKey('users.User', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug


class News(models.Model):

    # Relationship Fields
    article = models.OneToOneField('publications.Article', blank=True, null=True)
    chapter = models.ForeignKey('games.Chapter', blank=True, null=True)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.id