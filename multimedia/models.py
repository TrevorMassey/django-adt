from django.db import models
from filer.fields.image import FilerImageField
from django_extensions.db.fields import AutoSlugField


class Screenshot(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True)
    views = models.IntegerField(default=0) #
    created = models.DateTimeField(auto_now_add=True)
    image = FilerImageField(related_name="screenshot")

    # Relationships
    poster = models.ForeignKey('users.User')
    chapter = models.ForeignKey('games.Chapter')
    involved = models.ManyToManyField('users.User', blank=True, null=True, related_name='screenshots')

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.title

def quote_image_path(instance, filename):
    path, ext = filename.split('.')
    return 'images/quotes/{filename}.{ext}'.format(filename=instance.title, ext=ext)

class Quote(models.Model):

    INTERNAL = 'internal'
    EXTERNAL = 'external'

    QUOTE_TYPE = (
        (INTERNAL, 'internal source'),
        (EXTERNAL, 'external source'),
    )

    # Fields
    title = models.CharField(max_length=255)
    body = models.TextField()
    type = models.CharField(max_length=15, choices=QUOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=quote_image_path, blank=True, null=True)

    # Relationships
    poster = models.ForeignKey('users.User')
    involved = models.ManyToManyField('users.User', blank=True, null=True, related_name='quotes')

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.title
