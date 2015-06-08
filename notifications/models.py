from django.db import models


class Notification(models.Model):

    # Choices
    USERNAME_MENTION_COMMENT = 'username_mention_comment'
    USERNAME_MENTION_FORUM = 'username_mention_forum'
    APPLICATION = 'application'
    AWARD = 'award'
    PROMOTION = 'promotion'
    DEMOTION = 'demotion'
    EVENT = 'event'
    KICKED = 'kicked'
    QUOTE = 'quote'
    SCREENSHOT = 'screenshot'
    CHAPTER = 'chapter'

    NOTIFICATION_TYPES = (
        (USERNAME_MENTION_COMMENT, 'Username Mentioned in Comment'),
        (USERNAME_MENTION_FORUM, 'Username Mentioned in Forum Post'),
        (APPLICATION, 'Application Status Change'),
        (AWARD, 'Received Award'),
        (PROMOTION, 'Received Promotion'),
        (DEMOTION, 'Received Demotion'),
        (EVENT, 'New Event'),
        (KICKED, 'Kicked from guild'),
        (QUOTE, 'You were quoted'),
        (SCREENSHOT, 'You were tagged in a screenshot'),
        (CHAPTER, 'You were added to a chapter'),
    )

    # Fields
    type = models.CharField(max_length=30, choices=NOTIFICATION_TYPES)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    # Relationships
    user = models.ForeignKey('users.User', related_name='notifications')
    creator = models.ForeignKey('users.User', blank=True, null=True, related_name='+')

    application = models.ForeignKey('applications.Application', blank=True, null=True)
    rank = models.ForeignKey('users.Rank', blank=True, null=True)
    award = models.ForeignKey('awards.Award', blank=True, null=True)
    chapter = models.ForeignKey('games.Chapter', blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.user,)
