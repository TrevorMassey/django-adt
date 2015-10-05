from datetime import datetime
from django.core.files import File
import os
from django.core.management.base import BaseCommand
from django.db.models import Q
from django.utils import timezone
from applications.models import Application, ApplicationQuestion
from awards.models import AwardCategory, AwardImage, AwardType, AwardRecipient, Award
from games.models import Game, Chapter, ChapterMember
from publications.models import Article, News
from multimedia.models import Screenshot

from legacy.addict_website.models import GamesList as LegacyChapter
from legacy.addict_website.models import GamesPlaying as LegacyChapterMember
from legacy.addict_website.models import News as LegacyNews
from legacy.addict_website.models import Screenshots as LegacyScreenshot
from legacy.addict_website.models import Applications as LegacyApplication
from legacy.addict_forum.models import Phpbb3MedalsCats as LegacyAwardCategory
from legacy.addict_forum.models import Phpbb3Medals as LegacyAward
from legacy.addict_forum.models import Phpbb3MedalsAwarded as LegacyAwardAwarded



class Command(BaseCommand):

    def handle(self, *args, **options):
        self.migrate_chapters()

    def migrate_chapters(self):

        AwardType.objects.all().delete()
        awardtype = AwardType()
        awardtype.name = "Ribbon"
        awardtype.save()
        self.stdout.write("Created base Ribbon Type")

        AwardImage.objects.all().delete()
        for legacy_award in LegacyAward.objects.distinct():
                assert isinstance(legacy_award, LegacyAward)

                current_dir = os.path.dirname(os.path.realpath(__file__))
                image_dir = os.path.join(current_dir, '../../static/img/awards/')

                awardimg = AwardImage()
                awardimg.title = legacy_award.name

                file_path = os.path.abspath(os.path.join(image_dir, legacy_award.image))

                with open(file_path) as f:
                    awardimg.image = File(f)
                    awardimg.save()

        self.stdout.write("Created award Images")
        Game.objects.all().delete()
        Chapter.objects.all().delete()
        Article.objects.all().delete()
        ChapterMember.objects.all().delete()
        AwardCategory.objects.all().delete()
        Award.objects.all().delete()
        AwardRecipient.objects.all().delete()
        ApplicationQuestion.objects.all().delete()

        for legacy_chapter in LegacyChapter.objects.all():
            assert isinstance(legacy_chapter, LegacyChapter)

            existing_game = Game.objects.filter(Q(title=legacy_chapter.game_name))

            if existing_game:
                self.stdout.write("Duplicate game for id {id}".format(id=legacy_chapter.record))
                continue

            # if 0 (blank) make it blank
            if legacy_chapter.launch > 0:
                date_naive = datetime.utcfromtimestamp(legacy_chapter.launch)
                launch_date = timezone.make_aware(date_naive, timezone.utc)
            else:
                launch_date = None

            if legacy_chapter.close > 0:
                date_naive = datetime.utcfromtimestamp(legacy_chapter.close)
                close_date = timezone.make_aware(date_naive, timezone.utc)
            else:
                close_date = None

            # if its the No Game record, make it blank  --REMOVED
            # if legacy_chapter.record != -1:
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
            # else:
            #    chapter = None

            self.stdout.write("Created Chapter")

            for legacy_chapter_member in LegacyChapterMember.objects.filter(game=legacy_chapter.record):
                assert isinstance(legacy_chapter_member, LegacyChapterMember)

                date_naive = datetime.utcfromtimestamp(legacy_chapter_member.start)
                start_date = timezone.make_aware(date_naive, timezone.utc)

                if legacy_chapter.close > 0:
                    date_naive = datetime.utcfromtimestamp(legacy_chapter_member.stop)
                    stop_date = timezone.make_aware(date_naive, timezone.utc)
                else:
                    stop_date = None

                chapter_member = ChapterMember()
                chapter_member.member_id = legacy_chapter_member.userrecord
                chapter_member.chapter = chapter
                chapter_member.join_date = start_date
                chapter_member.leave_date = stop_date
                chapter_member.save()

            self.stdout.write("Created Chapter Members")

            for legacy_news in LegacyNews.objects.filter(game=legacy_chapter.record):
                assert isinstance(legacy_news, LegacyNews)

                date_naive = datetime.utcfromtimestamp(legacy_news.date)
                news_date = timezone.make_aware(date_naive, timezone.utc)

                article = Article()
                article.title = legacy_news.title
                article.body = legacy_news.news
                article.created = news_date
                article.author_id = legacy_news.creator
                article.save()

                news = News()
                news.title = article.title
                news.image = legacy_news.image
                news.article = article
                news.chapter = chapter
                news.save()

            self.stdout.write("Created News")

            for legacy_screenshot in LegacyScreenshot.objects.filter(category=legacy_chapter.record):
                assert isinstance(legacy_screenshot, LegacyScreenshot)

                date_naive = datetime.utcfromtimestamp(legacy_screenshot.timestamp)
                date = timezone.make_aware(date_naive, timezone.utc)

                screenshot = Screenshot()
                screenshot.title = legacy_screenshot.title
                screenshot.views = legacy_screenshot.views
                screenshot.created = date

                screenshot.image = "images/screenshots/{}.{}".format(legacy_screenshot.record, legacy_screenshot.type)
                screenshot.poster_id = legacy_screenshot.poster
                screenshot.chapter = chapter
                screenshot.save()

            self.stdout.write("Created Screenshots")

            for legacy_awardcategory in LegacyAwardCategory.objects.filter(game_id=legacy_chapter.record):
                assert isinstance(legacy_awardcategory, LegacyAwardCategory)

                awardcat = AwardCategory()
                awardcat.title = legacy_awardcategory.name
                awardcat.order = legacy_awardcategory.order_id
                awardcat.chapter = chapter

                awardcat.save()

                self.stdout.write("Created award category")

                for legacy_award in LegacyAward.objects.filter(parent=legacy_awardcategory.id):
                    assert isinstance(legacy_award, LegacyAward)
                    award = Award()
                    award.title = legacy_award.name
                    award.level_limit = legacy_award.number
                    award.order = legacy_award.order_id
                    award.description = legacy_award.description
                    award.category = awardcat
                    award.type = awardtype

                    img_lookup = AwardImage.objects.filter(title=legacy_award.name).order_by('-image')
                    award.image = img_lookup[0]

                    award.save()

                    self.stdout.write("Created award")

                    for legacy_award_recipient in LegacyAwardAwarded.objects.filter(medal_id=legacy_award.id):
                        assert isinstance(legacy_award_recipient, LegacyAwardAwarded)

                        date_naive = datetime.utcfromtimestamp(legacy_award_recipient.time)
                        date = timezone.make_aware(date_naive, timezone.utc)

                        award_recipient = AwardRecipient()
                        award_recipient.reason = legacy_award_recipient.nominated_reason
                        award_recipient.created = date
                        award_recipient.award = award
                        award_recipient.awarder_id = legacy_award_recipient.awarder_id
                        award_recipient.recipient_id = legacy_award_recipient.user_id

                        award_recipient.save()

                    self.stdout.write("Created award recipients")

            self.stdout.write("Finished Award stuff")

            if chapter is not None:

                app_question = ApplicationQuestion()
                app_question.question = 'Please list any previous guild experience.'
                app_question.order = 1
                app_question.chapter = chapter
                app_question.save()

                app_question = ApplicationQuestion()
                app_question.question = 'Are you comfortable repeating game content to progress the guild or other members? Please provide an example.'
                app_question.order = 2
                app_question.chapter = chapter
                app_question.save()

                app_question = ApplicationQuestion()
                app_question.question = 'Please describe your personality and social expectations within a guild atmosphere.'
                app_question.order = 3
                app_question.chapter = chapter
                app_question.save()

                app_question = ApplicationQuestion()
                app_question.question = 'Do you have any aspirations to leadership positions within the guild?'
                app_question.order = 4
                app_question.chapter = chapter
                app_question.save()

                app_question = ApplicationQuestion()
                app_question.question = 'What do you expect from your guild?'
                app_question.order = 5
                app_question.chapter = chapter
                app_question.save()

                app_question = ApplicationQuestion()
                app_question.question = 'Please describe the "best" way to level your character in the previous MMO you played from personal experience.'
                app_question.order = 6
                app_question.chapter = chapter
                app_question.save()

                self.stdout.write("Finished Application questions")

            # for legacy_application in LegacyApplication.objects.filter(game=legacy_chapter.id):
            #     assert isinstance(legacy_application, LegacyApplication)
            #
            #     date_naive = datetime.utcfromtimestamp(legacy_application.appdate)
            #     date = timezone.make_aware(date_naive, timezone.utc)
            #
            #     app = Application()
            #
            #     app.save()
        self.stdout.write("Import Successful.  Please note you will need to delete duplicate AwardImages and their "
                          "corresponding files in Media.")
