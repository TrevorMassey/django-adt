from django.db import models

class Review(models.Model):

    user = models.ForeignKey('users.User', related_name='+')
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', related_name='+')

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.user

class Vote(models.Model):

    YES = 'yes'
    NO = 'no'
    PASS = 'pass'

    VOTES = (
        (YES, 'Yes'),
        (NO, 'No'),
        (PASS, 'Unknown Member'),
    )

    review = models.ForeignKey('reviews.Review', related_name='votes')
    vote = models.CharField(max_length=15, choices=VOTES)

    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', related_name='+')

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.vote
