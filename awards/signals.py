from django.db.models.signals import post_save
from django.dispatch import receiver

from activityfeed.models import FeedItem
from awards.models import AwardRecipient


@receiver(post_save, sender=AwardRecipient)
def create_award_feed_item(sender, instance, created, **kwargs):

    if created:
        feed_item = FeedItem()
        feed_item.user_id = instance.recipient_id
        feed_item.type = FeedItem.AWARD
        feed_item.award_id = instance.award_id
        feed_item.save()
