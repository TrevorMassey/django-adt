from django.contrib.contenttypes.models import ContentType
from django.db import models, transaction
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django_extensions.db.fields import AutoSlugField
from users.models import User


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

    topic_count = models.PositiveIntegerField(default=0)
    post_count = models.PositiveIntegerField(default=0)

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
        ordering = ('order',)

    class MPTTMeta:
        order_insertion_by = 'order'

    def __unicode__(self):
        return u'%s' % self.title


class TopicManager(models.Manager):

    def create_topic(self, poster, forum, title, body, is_announcement=False, is_pinned=False, poll=None):
        """
        Creates a topic and associated post
        """

        with transaction.atomic():
            topic = Topic()
            topic.forum = forum
            topic.title = title
            topic.is_announcement = is_announcement
            topic.is_pinned = is_pinned
            topic.starter = poster

            if poll is not None:
                topic.is_poll = True

            topic.save()

            Post.objects.create_post(poster=poster, topic=topic, body=body)

        return topic


class Topic(models.Model):

    # Fields
    forum = models.ForeignKey('forums.Forum', related_name='topics')
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

    # Latest reply
    last_post_on = models.DateTimeField(db_index=True)
    last_post = models.ForeignKey('forums.Post', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)

    # Deleted
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey('users.User', blank=True, null=True, related_name='+', on_delete=models.SET_NULL)
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

    def reply(self, poster, body):
        post = Post.objects.create_post(poster=poster, topic=self, body=body)
        return post


class PostManager(models.Manager):

    def create_post(self, poster, topic, body):
        """
        Creates post for a given user under an existing topic
        """

        post = Post()
        post.forum = topic.forum
        post.thread = topic
        post.body = body
        post.poster = poster
        post.save()

        return post

class Post(models.Model):
    forum = models.ForeignKey('forums.Forum', related_name='posts')
    thread = models.ForeignKey('forums.Topic', related_name='posts')
    poster = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    posted = models.DateTimeField(auto_now_add=True)

    # mentions = models.ManyToManyField('users.User', related_name="mention_set")

    # Edits
    updated = models.DateTimeField(blank=True, null=True)
    edits = models.PositiveIntegerField(default=0)
    last_editor = models.ForeignKey('users.User', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)

    # Deleted
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey('users.User', related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
    deleted_time = models.DateTimeField(blank=True, null=True)

    objects = PostManager()

    class Meta:
        ordering = ('-created',)
        permissions = (
            ('soft_delete_post', 'Can soft delete post'),
        )

    def __unicode__(self):
        return '%s...' % self.body[10:].strip()

    def edit(self, body, editor):

        post = Post.objects.select_for_update().get(id=self.id)
        post.body = body
        post.edits += 1
        post.last_editor = editor
        post.updated = timezone.now()
        post.save()

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
