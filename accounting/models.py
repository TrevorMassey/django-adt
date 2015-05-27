from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django_extensions.db.fields import AutoSlugField


class DonateAmount(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    # Relationship Fields
    user = models.OneToOneField('users.User',)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.id


class DonateCost(models.Model):

    # Fields
    service = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='service', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug
