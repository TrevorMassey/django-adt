from django_extensions.db.fields import AutoSlugField
from django.db import models

class Award(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True, unique=True)
    level_limit = models.IntegerField()
    order = models.IntegerField()
    description = models.TextField()

    # Relationship Fields
    category = models.ForeignKey('awards.AwardCategory',)
    image = models.ForeignKey('awards.AwardImage')
    type = models.ForeignKey('awards.AwardType', )

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug


class AwardType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = AutoSlugField(populate_from='name', blank=True, unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class AwardCategory(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True, unique=True)
    order = models.IntegerField()

    # Relationship Fields
    chapter = models.ForeignKey('games.Chapter',)

    class Meta:
        ordering = ('-id',)
        unique_together = (
            ('title', 'chapter'),
        )

    def __unicode__(self):
        return u'%s' % self.slug


class AwardRecipient(models.Model):

    # Fields
    reason = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    # Relationship Fields
    award = models.ForeignKey('awards.Award',)

    awarder = models.ForeignKey('users.User', related_name='awarded')
    recipient = models.ForeignKey('users.User', related_name='award_recipients')

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.id


def award_image_path(instance, filename):
    path, ext = filename.split('.')
    return 'images/awards/{filename}.{ext}'.format(filename=instance.slug, ext=ext)


class AwardImage(models.Model):

    # Fields
    title = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='title', blank=True, unique=True)
    image = models.ImageField(upload_to=award_image_path)

    def __unicode__(self):
        return u'%s' % self.title
