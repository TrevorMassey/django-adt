from django.contrib.contenttypes.models import ContentType
from django_extensions.db.fields import AutoSlugField
from django.db import models

class Award(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    level_limit = models.IntegerField()
    order = models.IntegerField()
    description = models.TextField()

    # Relationship Fields
    category = models.ForeignKey('awards.AwardCategory', related_name='awards')
    image = models.ForeignKey('awards.AwardImage')
    type = models.ForeignKey('awards.AwardType', )

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.title

# TODO might not need slug
class AwardType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class AwardCategory(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    order = models.IntegerField()

    # Relationship Fields
    chapter = models.ForeignKey('games.Chapter', related_name='award_categories', blank=True, null=True)

    class Meta:
        verbose_name = 'award category'
        verbose_name_plural = 'award categories'
        ordering = ('-id',)
        unique_together = (
            ('title', 'chapter'),
        )

    def __unicode__(self):
        return u'%s' % self.slug


class AwardRecipient(models.Model):

    # Fields
    reason = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    # Relationship Fields
    award = models.ForeignKey('awards.Award', related_name='award_recipient')

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
    slug = AutoSlugField(populate_from='title', unique=True)
    image = models.ImageField(upload_to=award_image_path)

    def __unicode__(self):
        return u'%s' % self.title


class Achievement(models.Model):

    CREATED = 0
    RAIDS = 1
    WHATEVER = 2

    ACTION_CHOCIES = (
        (CREATED, 'Created'),
        (RAIDS, 'Raids'),
        (WHATEVER, 'Whatever'),
    )

    action = models.CharField(choices=ACTION_CHOCIES)
    count = models.PositiveIntegerField(blank=True, null=True)
    award = models.ForeignKey('awards.Award')
    item = models.ForeignKey(ContentType)
