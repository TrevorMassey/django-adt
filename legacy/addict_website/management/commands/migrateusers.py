from datetime import datetime
import logging
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.utils import timezone
from publications.models import Article, News

from users.models import User
from legacy.addict_website.models import Users as LegacyUser
from legacy.addict_website.models import News as LegacyNews


logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.migrate_users()

    def migrate_users(self):
        User.objects.all().delete()

        new_users = []

        for legacy_user in LegacyUser.objects.all():
            assert isinstance(legacy_user, LegacyUser)

            reg_date_naive = datetime.utcfromtimestamp(legacy_user.regdate)
            reg_date = timezone.make_aware(reg_date_naive, timezone.utc)

            existing_user = User.objects.filter(Q(email=legacy_user.email) | Q(username=legacy_user.username))

            if existing_user:
                self.stdout.write("Duplicate user for id {id}".format(id=legacy_user.record))
                continue

            user = User()
            user.id = legacy_user.record
            user.email = legacy_user.email
            user.username = legacy_user.username
            user.display_name = legacy_user.username
            if legacy_user.rank > 19:
                legacy_user.rank = 19
            if legacy_user.rank >= 0:
                user.rank_id = legacy_user.rank + 1
            user.date_joined = reg_date
            user.ts_uid = legacy_user.tsuid
            if user.username == "Gromph" or user.username == "unkle" or user.username == "mrbaboon":
                user.is_superuser = True
                user.is_staff = True
            user.save()

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
            news.save()
