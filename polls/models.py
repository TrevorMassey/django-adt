from django.db import models
from django_extensions.db.fields import AutoSlugField


class Poll(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'poll'
        verbose_name_plural = 'polls'

    def __unicode__(self):
        return self.title

    # TODO optimize this, or count item counts on frontend
    # def get_vote_count(self):
    #     return Vote.objects.filter(poll=self).count()
    # vote_count = property(fget=get_vote_count)


class Item(models.Model):

    # Fields
    answer = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    # Relationships
    poll = models.ForeignKey('polls.Poll', related_name='items')

    class Meta:
        verbose_name = 'choice'
        verbose_name_plural = 'choices'
        ordering = ['order']

    def __unicode__(self):
        return u'%s' % (self.answer,)

    # TODO optimize this
    def get_vote_count(self):
        return Vote.objects.filter(item=self).count()
    vote_count = property(fget=get_vote_count)


class Vote(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True)

    # Relationships
    poll = models.ForeignKey('polls.Poll')
    item = models.ForeignKey('polls.Item')
    user = models.ForeignKey('users.User')

    class Meta:
        verbose_name = 'vote'
        verbose_name_plural = 'votes'

    def __unicode__(self):
        return u'%s' % (self.user,)
