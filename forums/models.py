from django.db import models
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django_extensions.db.fields import AutoSlugField


class Forum(MPTTModel):

    # Choices
    CATEGORY = 'category'
    FORUM = 'forum'
    LINK = 'link'

    FORUM_TYPES = (
        (CATEGORY, 'category'),
        (FORUM, 'forum'),
        (LINK, 'link'),
    )

    # Fields
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=15, choices=FORUM_TYPES)
    link_url = models.URLField(blank=True, null=True)

    order = models.PositiveIntegerField(default=0)

    topics = models.PositiveIntegerField(default=0)
    posts = models.PositiveIntegerField(default=0)

    # Latest post info
    last_post_on = models.DateTimeField(null=True, blank=True)
    last_thread = models.ForeignKey('forums.Topic', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
    last_thread_title = models.CharField(max_length=255, null=True, blank=True)
    last_thread_slug = models.CharField(max_length=255, null=True, blank=True)
    last_poster = models.ForeignKey('users.User', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
    last_poster_name = models.CharField(max_length=255, null=True, blank=True)
    last_poster_avatar = models.CharField(max_length=255, null=True, blank=True)
    last_poster_rank_color = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('-title',)

    class MPTTMeta:
        order_insertion_by = 'order'

    def __unicode__(self):
        return u'%s' % self.title


class TopicManager(models.Manager):
    pass


class Topic(models.Model):

    # Fields
    forum = models.ForeignKey('forums.Forum')
    label = models.ForeignKey('forums.Label', blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    replies = models.PositiveIntegerField(default=0, db_index=True)
    views = models.PositiveIntegerField(default=0)

    is_announcement = models.BooleanField(default=False, db_index=True)
    is_pinned = models.BooleanField(default=False, db_index=True)

    is_poll = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)

    # Topic starter
    first_post = models.ForeignKey('forums.Post', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
    starter = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.SET_NULL)
    starter_name = models.CharField(max_length=255)
    starter_avatar = models.CharField(max_length=255, null=True, blank=True)
    starer_rank_color = models.CharField(max_length=255, null=True, blank=True)

    # Latest reply
    last_post_on = models.DateTimeField(db_index=True)
    last_post = models.ForeignKey('forums.Post', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
    last_poster = models.ForeignKey('users.User', related_name='last_poster_set', null=True, blank=True, on_delete=models.SET_NULL)
    last_poster_name = models.CharField(max_length=255, null=True, blank=True)
    last_poster_avatar = models.CharField(max_length=255, null=True, blank=True)
    last_poster_rank_color = models.CharField(max_length=255, null=True, blank=True)

    # Deleted
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey('users.User', blank=True, null=True, related_name='+', on_delete=models.SET_NULL)
    deleted_by_name = models.CharField(max_length=255, null=True, blank=True)
    deleted_time = models.DateTimeField(blank=True, null=True)

    objects = TopicManager()

    class Meta:
        index_together = [
            ['forum', 'id'],
            ['forum', 'last_post_on'],
            ['forum', 'replies'],
        ]
        permissions = (
            ('soft_delete_topic', 'Can soft delete topic'),
        )

    def __unicode__(self):
        return u'%s' % self.title

    def soft_delete(self, user):
        self.deleted_by = user
        self.is_deleted = True
        self.deleted_time = timezone.now()
        self.save()



class Post(models.Model):
    forum = models.ForeignKey('forums.Forum')
    thread = models.ForeignKey('forums.Topic')

    poster = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.SET_NULL)
    poster_name = models.CharField(max_length=255)
    poster_avatar = models.CharField(max_length=255, null=True, blank=True)
    poster_rank_color = models.CharField(max_length=255, null=True, blank=True)
    poster_signature = models.CharField(max_length=255, null=True, blank=True)

    body = models.TextField()

    posted = models.DateTimeField(auto_now_add=True)

    # mentions = models.ManyToManyField('users.User', related_name="mention_set")

    # Edits
    updated = models.DateTimeField(blank=True, null=True)
    edits = models.PositiveIntegerField(default=0)
    last_editor = models.ForeignKey('users.User', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
    last_editor_name = models.CharField(max_length=255, null=True, blank=True)
    last_editor_avatar = models.CharField(max_length=255, null=True, blank=True)
    last_editor_rank_color = models.CharField(max_length=255, null=True, blank=True)

    # Deleted
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey('users.User', related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
    deleted_by_name = models.CharField(max_length=255, null=True, blank=True)
    deleted_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-created',)
        permissions = (
            ('soft_delete_post', 'Can soft delete post'),
        )

    def __unicode__(self):
        return '%s...' % self.original[10:].strip()

    def soft_delete(self, user):
        self.deleted_by = user
        self.is_deleted = True
        self.deleted_time = timezone.now()
        self.save()



class Label(models.Model):
    # Prefix label instead of tags for threads
    forums = models.ManyToManyField('forums.Forum')
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', blank=True)
    css_class = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.title
