from datetime import datetime
import logging
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.utils import timezone
from publications.models import Article, News

from legacy.addict_website.models import News as LegacyNews


logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.migrate_news()

    def migrate_news(self):

        for legacy_news in LegacyNews.objects.all():
            assert isinstance(legacy_news, LegacyNews)

            date_naive = datetime.utcfromtimestamp(legacy_news.date)
            date = timezone.make_aware(date_naive, timezone.utc)

            article = Article()
            article.title = legacy_news.title
            article.body = legacy_news.news
            article.created = date
            article.author_id = legacy_news.creator
            article.save()

            news = News()
            news.title = article.title
            news.image = legacy_news.image
            news.article = article
            # news.chapter_id = legacy_news.game (needs to map to new id's)
            news.save()
