from django.db.models.signals import post_save
from django.dispatch import receiver

from activityfeed.models import FeedPost, FeedItem

@receiver(post_save, sender=FeedPost)
def create_feed_post_feed_item(sender, instance, created, **kwargs):

    if created:
        feed_item = FeedItem()
        feed_item.user_id = instance.author_id
        feed_item.type = FeedItem.FEED_POST
        feed_item.feed_post = instance
        feed_item.save()