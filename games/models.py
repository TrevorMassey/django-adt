from django.db import models
from django_extensions.db.fields import AutoSlugField


class Chapter(models.Model):

    # Fields
    open_date = models.DateTimeField()
    launch_date = models.DateTimeField()
    close_date = models.DateTimeField()

    # Relationship Fields
    members = models.ManyToManyField('users.User',)
    game = models.ForeignKey('games.Game',)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.id


# Create your models here.
class Game(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug

