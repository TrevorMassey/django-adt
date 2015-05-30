from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django_extensions.db.fields import AutoSlugField


class Guild(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

class Role(models.Model):

    # Fields
    role = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='role', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    duration = models.IntegerField()

    # Relationship Fields
    guild = models.ForeignKey('dossiers.Guild',)
    game = models.ForeignKey('games.Game',)
    application = models.ForeignKey('applications.Application', blank=True, null=True)
    # TODO: This either needs to relate to a user directly, or a global
    # dossier directly as we can add Games, Guilds, and Roles to
    # a dossier that is created for someone who has not applied

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug
