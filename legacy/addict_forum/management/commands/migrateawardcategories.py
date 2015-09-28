from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
from games.models import Chapter
from multimedia.models import Screenshot

from legacy.addict_forum.models import Phpbb3MedalsCats as LegacyAwardCategory


# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         self.migrate_awardcategories()
#
#     def migrate_awardcategories(self):
#
#         for legacy_awardcategories in LegacyAwardCategory.objects.all():
#             assert isinstance(legacy_screenshot, LegacyScreenshot)
#
#             date_naive = datetime.utcfromtimestamp(legacy_screenshot.timestamp)
#             date = timezone.make_aware(date_naive, timezone.utc)
#
#             screenshot = Screenshot()
#             screenshot.title = legacy_screenshot.title
#             screenshot.views = legacy_screenshot.views
#             screenshot.created = date
#
#             screenshot.image = "images/screenshots/{}.{}".format(legacy_screenshot.record, legacy_screenshot.type)
#             screenshot.poster_id = legacy_screenshot.poster
#
#             category = ScreenshotsCats.objects.filter(record=legacy_screenshot.category).all()
#             chapter = Chapter.objects.filter(title=category.title)  # Y U NO WERK
#             screenshot.chapter_id = chapter
#
#             screenshot.save()

