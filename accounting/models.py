from django.db import models
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
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug


class DonateGoal(models.Model):

    # Fields
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    end = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.amount
