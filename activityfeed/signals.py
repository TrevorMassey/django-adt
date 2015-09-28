from django.db.models.signals import post_save
from django.dispatch import receiver

from swampdragon.pubsub_providers.data_publisher import publish_data

from activityfeed.models import FeedPost, FeedItem

from activityfeed.serializers import FeedPostSerializer

@receiver(post_save, sender=FeedPost)
def create_feed_post_feed_item(sender, instance, created, **kwargs):

    if created:
        feed_item = FeedItem()
        feed_item.user_id = instance.author_id
        feed_item.type = FeedItem.FEED_POST
        feed_item.feed_post = instance
        feed_item.save()


@receiver(post_save, sender=FeedPost)
def send_swampdragon_push(sender, instance, created, **kwargs):

    if created:

        serializer = FeedPostSerializer(instance=instance)

        publish_data(channel='post-24', data=serializer.data)
