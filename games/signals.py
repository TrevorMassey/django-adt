from django.db.models.signals import post_save
from django.dispatch import receiver

from activityfeed.models import FeedItem
from games.models import Chapter, ChapterMember
from notifications.models import Notification


@receiver(post_save, sender=Chapter)
def create_chapter_feed_item(sender, instance, created, **kwargs):

    if created:
        feed_item = FeedItem()
        feed_item.user_id = instance.creator_id
        feed_item.type = FeedItem.NEW_CHAPTER
        feed_item.chapter = instance
        feed_item.save()

@receiver(post_save, sender=ChapterMember)
def create_chapter_member_feed_item(sender, instance, created, **kwargs):

    if created:
        feed_item = FeedItem()
        feed_item.user_id = instance.member_id
        feed_item.type = FeedItem.JOIN_CHAPTER
        feed_item.chapter_id = instance.chapter_id
        feed_item.save()

@receiver(post_save, sender=ChapterMember)
def create_chapter_notification(sender, instance, created, **kwargs):

    if created:
        notification = Notification()
        notification.user_id = instance.member_id
        notification.type = Notification.JOIN_CHAPTER
        notification.chapter_id = instance.chapter_id
        notification.save()
