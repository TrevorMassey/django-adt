from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.db.models import Q
from django.utils import timezone
from comments.models import Comment

from legacy.addict_website.models import Comments as LegacyComment

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.migrate_comments()

    def migrate_comments(self):

        for legacy_comment in LegacyComment.objects.all():
            assert isinstance(legacy_comment, LegacyComment)

            date_naive = datetime.utcfromtimestamp(legacy_comment.timestamp)
            date = timezone.make_aware(date_naive, timezone.utc)

            comment = Comment()
            comment.body = legacy_comment.comment
            comment.created = date
            comment.public = not legacy_comment.officer

            comment.user_id = legacy_comment.poster_id  # this is erroring

            if legacy_comment.section == 0:
                continue
            if legacy_comment.section == 1:
                continue
            if legacy_comment.section == 2:
                continue
            if legacy_comment.section == 5:
                continue

            comment.content_type_id = {  # i dont know what the keys are for the different content types
                0: 1,  # user manager
                1: 2,  # application
                2: 3,  # fodder vote
                3: 4,  # quote
                4: 5,  # screenshot
                5: 6   # leadership application
            }.get(legacy_comment.section)

            comment.object_id = legacy_comment.reference
            comment.save()
