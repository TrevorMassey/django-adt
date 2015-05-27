from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django_extensions.db.fields import AutoSlugField


class Guild(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    # Relationship Fields
    game = models.OneToOneField('games.Game',)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

class Role(models.Model):

    # Fields
    role = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    duration = models.IntegerField()

    # Relationship Fields
    guild = models.ForeignKey('dossiers.Guild',)
    game = models.ForeignKey('games.Game',)
    application = models.ForeignKey('applications.Application',)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug
