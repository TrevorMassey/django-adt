import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from activityfeed.models import FeedItem
from notifications.models import Notification
from users.models import User

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def create_rank_feed_item(sender, instance, created, **kwargs):

    old_rank = instance.rank_tracker.changed().get('rank')

    if old_rank:

        feed_item = FeedItem()

        if old_rank < instance.rank_id:
            # promotion
            feed_item.type = FeedItem.PROMOTION

        if old_rank > instance.rank_id:
            # demotion
            feed_item.type = FeedItem.DEMOTION

        if instance.rank_id is None:
            # kicked
            feed_item.type = Notification.KICKED

        feed_item.user = instance
        feed_item.rank_id = instance.rank_id
        feed_item.save()

@receiver(post_save, sender=User)
def create_rank_notification(sender, instance, created, **kwargs):

    old_rank = instance.rank_tracker.changed().get('rank')

    if old_rank:

        notification = Notification()

        if old_rank < instance.rank_id:
            # promotion
            notification.type = Notification.PROMOTION

        if old_rank > instance.rank_id:
            # demotion
            notification.type = Notification.DEMOTION

        if instance.rank_id is None:
            # kicked
            notification.type = Notification.KICKED

        notification.user = instance
        notification.rank_id = instance.rank_id
        notification.save()
