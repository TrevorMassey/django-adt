from django.db.models.signals import post_save
from django.dispatch import receiver
from activityfeed.models import FeedItem
from multimedia.models import Screenshot, Quote


@receiver(post_save, sender=Screenshot)
def create_screenshot_feed_item(sender, instance, created, **kwargs):

    if created:
        feed_item = FeedItem()
        feed_item.user_id = instance.poster_id
        feed_item.type = FeedItem.SCREENSHOT
        feed_item.screenshot = instance
        feed_item.save()

@receiver(post_save, sender=Quote)
def create_quote_feed_item(sender, instance, created, **kwargs):

    if created:
        feed_item = FeedItem()
        feed_item.user_id = instance.poster_id
        feed_item.type = FeedItem.QUOTE
        feed_item.quote = instance
        feed_item.save()
