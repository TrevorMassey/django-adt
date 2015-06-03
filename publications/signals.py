from django.db.models.signals import post_save
from django.dispatch import receiver

from activityfeed.models import FeedItem
from publications.models import News


@receiver(post_save, sender=News)
def create_news_feed_item(sender, instance, created, **kwargs):

    if created:
        feed_item = FeedItem()
        feed_item.user_id = instance.article.author_id
        feed_item.type = FeedItem.NEWS
        feed_item.news = instance
        feed_item.save()
