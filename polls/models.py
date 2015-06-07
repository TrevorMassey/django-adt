from django.db import models
from users.models import User


class Poll(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'poll'
        verbose_name_plural = 'polls'

    def __unicode__(self):
        return self.title

    def get_vote_count(self):
        return Vote.objects.filter(poll=self).count()
    vote_count = property(fget=get_vote_count)


class Item(models.Model):

    # Fields
    answer = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    # Relationships
    poll = models.ForeignKey(Poll)

    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'
        ordering = ['order']

    def __unicode__(self):
        return u'%s' % (self.answer,)

    def get_vote_count(self):
        return Vote.objects.filter(item=self).count()
    vote_count = property(fget=get_vote_count)


class Vote(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True)

    # Relationships
    poll = models.ForeignKey(Poll)
    item = models.ForeignKey(Item)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'vote'
        verbose_name_plural = 'votes'

    def __unicode__(self):
        return u'%s' % (self.user,)
