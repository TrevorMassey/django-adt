from django.db import models
from django.utils import timezone


class FeedPost(models.Model):
    author = models.ForeignKey('users.User', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    body = models.TextField()


class FeedItem(models.Model):

    FORUM_POST = 'forum_post'
    FEED_POST = 'feed_post'
    JOIN_CHAPTER = 'join_chapter'
    SCREENSHOT = 'screenshot'
    VIDEO = 'video'
    QUOTE = 'quote'
    NEW_CHAPTER = 'new_chapter'
    PROMOTION = 'promotion'
    DEMOTION = 'demotion'
    AWARD = 'award'
    NEWS = 'news'

    FEED_TYPES = (
        (FEED_POST, 'New Feed Post'),
        (FORUM_POST, 'New Forum Post'),
        (JOIN_CHAPTER, 'Joined Chapter'),
        (SCREENSHOT, 'Uploaded Screenshot'),
        (VIDEO, 'New Video'),
        (QUOTE, 'New Quote'),
        (NEW_CHAPTER, 'New Chapter'),
        (PROMOTION, 'Promoted'),
        (DEMOTION, 'Demoted'),
        (AWARD, 'New Award Recipient'),
        (NEWS, 'New News'),
    )

    user = models.ForeignKey('users.User')
    type = models.CharField(max_length=15, choices=FEED_TYPES)
    public = models.BooleanField(default=False)
    created = models.DateField(default=timezone.now)

    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey('users.User', blank=True, null=True, related_name='+')
    deleted_time = models.DateTimeField(blank=True, null=True)

    chapter = models.ForeignKey('games.Chapter', blank=True, null=True)
    news = models.ForeignKey('publications.News', blank=True, null=True)
    rank = models.ForeignKey('users.Rank', blank=True, null=True)
    feed_post = models.ForeignKey('activityfeed.FeedPost', blank=True, null=True)
    award = models.ForeignKey('awards.Award', blank=True, null=True)

    def __unicode__(self):
        return u'{user.get_full_name} - {type}'.format(user=self.user, type=self.get_type_display())

    class Meta:
        permissions = (
            ('soft_delete_feeditem', 'Can soft delete feed item'),
        )

    def soft_delete(self, user):
        self.deleted_by = user
        self.is_deleted = True
        self.deleted_time = timezone.now()
        self.save()

    # forum_post

    # Gromph posted a message <message body>
    # Excentric joined the guild for ArcheAge
    # Nadasdy added a screenshot, "Mediocre". <screenshot>
    # Yawgmoth added a new quote, "Quote title", "Quote body"
    # Gromph opened a new chapter for Star Citizen

    # USER   ACTION   TARGET