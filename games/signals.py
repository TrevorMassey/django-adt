import logging

from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from activityfeed.models import FeedItem
from games.models import Chapter

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Chapter)
def create_chapter_feed_item(sender, instance, created, **kwargs):

    if created:
        feed_item = FeedItem()
        feed_item.user_id = instance.creator_id
        feed_item.type = FeedItem.NEW_CHAPTER
        feed_item.chapter = instance
        feed_item.save()


