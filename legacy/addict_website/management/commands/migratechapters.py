from datetime import datetime
from django.core.management.base import BaseCommand
from django.db.models import Q
from django.utils import timezone
from games.models import Game, Chapter
from legacy.addict_website.models import GamesList as LegacyChapter



class Command(BaseCommand):

    def handle(self, *args, **options):
        self.migrate_chapters()

    def migrate_chapters(self):

        for legacy_chapter in LegacyChapter.objects.all():
            assert isinstance(legacy_chapter, LegacyChapter)

            existing_game = Game.objects.filter(Q(title=legacy_chapter.game_name))

            if existing_game:
                self.stdout.write("Duplicate game for id {id}".format(id=legacy_chapter.record))
                continue

            date_naive = datetime.utcfromtimestamp(legacy_chapter.launch)
            launch_date = timezone.make_aware(date_naive, timezone.utc)
            date_naive = datetime.utcfromtimestamp(legacy_chapter.close)
            close_date = timezone.make_aware(date_naive, timezone.utc)

            game = Game()
            game.title = legacy_chapter.game_name
            game.save()

            chapter = Chapter()
            chapter.game = game
            chapter.creator_id = 24
            chapter.open_date = launch_date
            chapter.launch_date = launch_date
            chapter.close_date = close_date
            chapter.save()
