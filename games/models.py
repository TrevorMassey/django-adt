from django.db import models
from django_extensions.db.fields import AutoSlugField


class Chapter(models.Model):

    # Fields
    open_date = models.DateTimeField(blank=True, null=True)
    launch_date = models.DateTimeField(blank=True, null=True)
    close_date = models.DateTimeField(blank=True, null=True)

    # Relationship Fields
    members = models.ManyToManyField('users.User', blank=True)
    game = models.ForeignKey('games.Game',)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.game


# Create your models here.
class Game(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.title

