from django.db import models
from django_extensions.db.fields import AutoSlugField


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
    join_date = models.DateTimeField(auto_now_add=True)
    leave_date = models.DateTimeField(blank=True, null=True)

    # Relationship Fields
    member = models.ForeignKey('users.User', related_name='chapters')
    chapter = models.ForeignKey('games.Chapter', related_name='members')


# Create your models here.
class Game(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.title
