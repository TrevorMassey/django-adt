from django.db import models
from django_extensions.db.fields import AutoSlugField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Chapter(models.Model):

    # Fields
    open_date = models.DateTimeField(blank=True, null=True)
    launch_date = models.DateTimeField(blank=True, null=True)
    close_date = models.DateTimeField(blank=True, null=True)

    # Relationship Fields
    game = models.ForeignKey('games.Game',)
    creator = models.ForeignKey('users.User', related_name='+')

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.game


class ChapterMember(models.Model):

    # Fields
    # TODO need slug field from game__title
    join_date = models.DateTimeField(auto_now_add=True)
    leave_date = models.DateTimeField(blank=True, null=True)

    role = models.CharField(max_length=255, blank=True, null=True)

    # Relationship Fields
    member = models.ForeignKey('users.User', related_name='chapters')
    chapter = models.ForeignKey('games.Chapter', related_name='members')
    division = models.ForeignKey('games.ChapterDivision',
                                 related_name='members', on_delete=models.SET_NULL,
                                 blank=True, null=True,)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.member

    # TODO:  if leave_date is set then division = null


class ChapterDivision(MPTTModel):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    order = models.IntegerField()

    # Relationship Fields
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    chapter = models.ForeignKey('games.Chapter', related_name='divisions')

    class Meta:
        ordering = ('-id',)

    class MPTTMeta:
        order_insertion_by = 'order'

    def __unicode__(self):
        return u'%s' % self.title


class Game(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.title
