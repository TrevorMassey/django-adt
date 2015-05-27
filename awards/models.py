from django_extensions.db.fields import AutoSlugField
from django.db import models


class Award(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    level_limit = models.IntegerField()
    order = models.IntegerField()
    description = models.TextField()
    image = models.FilePathField()

    # Relationship Fields
    category = models.ForeignKey('awards.AwardCategory',)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug


class AwardCategory(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    order = models.IntegerField()

    # Relationship Fields
    chapter = models.OneToOneField('games.Chapter',)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug


class AwardRecipient(models.Model):

    # Fields
    reason = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    # Relationship Fields
    award = models.ForeignKey('awards.Award',)
    awarder = models.ForeignKey('users.User',)
    recipient = models.ForeignKey('users.User',)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.id