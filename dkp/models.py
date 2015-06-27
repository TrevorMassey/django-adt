from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import models
from django_extensions.db.fields import AutoSlugField


class Location(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    description = models.TextField(blank=True, null=True)
    dkp = models.DecimalField(default=1, max_digits=10, decimal_places=2)

    game = models.ForeignKey('games.Game', related_name='+')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    def __unicode__(self):
        return u'%s' % (self.title,)


class Entity(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    dkp = models.DecimalField(default=1, max_digits=10, decimal_places=2)

    location = models.ForeignKey('dkp.Location', related_name='entities')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'entity'
        verbose_name_plural = 'entities'

    def __unicode__(self):
        return u'%s' % (self.title,)


class Item(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    entity = models.ForeignKey('dkp.Entity', related_name='items')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __unicode__(self):
        return u'%s' % (self.title,)


class Section(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)

    chapter = models.ForeignKey('games.Chapter', related_name='dkp_section')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'section'
        verbose_name_plural = 'sections'

    def __unicode__(self):
        return u'%s' % (self.title,)


class Bonus(models.Model):
    dkp = models.DecimalField(default=1,max_digits=10, decimal_places=2)

    section = models.ForeignKey('dkp.Section', related_name='bonus_dkp')
    user = models.ForeignKey('users.User', related_name='+')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'bonus'
        verbose_name_plural = 'bonuses'

    def __unicode__(self):
        return u'%s' % (self.dkp,)


class Resource(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    dkp = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    section = models.ForeignKey('dkp.Section', related_name='resources')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'resource'
        verbose_name_plural = 'resources'

    def __unicode__(self):
        return u'%s' % (self.title,)


class ResourceContrib(models.Model):
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', related_name='+')
    resource = models.ForeignKey('dkp.Resource', related_name='contributions')
    user = models.ForeignKey('users.User', related_name='+')
    dkp = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'resourcecontribution'
        verbose_name_plural = 'resourcecontributions'

    def __unicode__(self):
        return u'%s' % (self.user,)


class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', related_name='+')

    event_leader = models.ForeignKey('users.User', related_name='events_ran')

    section = models.ForeignKey('dkp.Section', related_name='events')
    location = models.ForeignKey('dkp.Location', related_name='events')

    started = models.DateTimeField(blank=True, null=True)
    stopped = models.DateTimeField(blank=True, null=True)

    scheduled = models.BooleanField(default=False)
    standby_rate = models.FloatField(default=0.5)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def __unicode__(self):
        return u'%s' % (self.title,)


class EventAttendance(models.Model):
    event = models.ForeignKey('dkp.Event', related_name='attendees')
    user = models.ForeignKey('users.User', related_name='event_attandance')

    started = models.DateTimeField(auto_now_add=True)
    stopped = models.DateTimeField(blank=True, null=True)

    standby = models.BooleanField(default=False)

    class Meta:
        ordering = ('-started',)
        verbose_name = 'eventattendance'
        verbose_name_plural = 'eventattendance'

    def __unicode__(self):
        return u'%s' % (self.user,)


class EventItem(models.Model):
    dkp = models.DecimalField(default=1, max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('users.User', related_name='awarded_items')
    item = models.ForeignKey('dkp.Item', related_name='awarded_items')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'eventitem'
        verbose_name_plural = 'eventitems'

    def __unicode__(self):
        return u'%s' % (self.item,)
    #
    # def save(self, **kwargs):
    #     super(EventItem, self).save(**kwargs)
    #     self.create_transaction()
    #
    # def create_transaction(self):
    #     Transaction.objects.create(event=self, credit=self.dkp, item=self.item, user=self.user)



class EventEntity(models.Model):
    event = models.ForeignKey('dkp.Event', related_name='entities')
    entity = models.ForeignKey('dkp.Entity', related_name='kills')
    created = models.DateTimeField(auto_now_add=True)
    dkp = models.DecimalField(default=1, max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'evententity'
        verbose_name_plural = 'evententities'

    def __unicode__(self):
        return u'%s' % (self.entity,)


class Transaction(models.Model):

    user = models.ForeignKey('users.User', related_name='dkp_transactions')

    credit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    debit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    bonus = models.ForeignKey('dkp.Bonus', related_name='+', blank=True, null=True)
    attendance = models.ForeignKey('dkp.EventAttendance', related_name='+', blank=True, null=True)
    item = models.ForeignKey('dkp.EventItem', related_name='+', blank=True, null=True)
    entity = models.ForeignKey('dkp.EventEntity', related_name='+', blank=True, null=True)
    resource_contrib = models.ForeignKey('dkp.ResourceContrib', related_name='+', blank=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'

    def __unicode__(self):
        return u'%s' % (self.user,)

    def clean(self):
        if self.credit and self.debit:
            raise ValidationError('Cannot have a credit and debit on single transaction.')
        if not self.credit and not self.debit:
            raise ValidationError('Cannot have an empty or zero transaction.')
        if self.credit == Decimal("0.0"):
            raise ValidationError('Cannot have a transaction credit of zero.')
        if self.debit == Decimal("0.0"):
            raise ValidationError('Cannot have a transaction debit of zero.')
