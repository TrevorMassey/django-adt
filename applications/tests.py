import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import User, Game, Rank, Chapter, Award, AwardCategory, AwardRecipient, Codex, Article, News, DonateAmount, DonateCost, Application, ApplicationQuestion, ApplicationAnswer, DossierGuild, DossierRole


def create_user(**kwargs):
    defaults = {}
    defaults["display_name"] = "display_name"
    defaults["slug"] = "slug"
    defaults["email"] = "email"
    defaults["signed_in"] = "signed_in"
    defaults["password"] = "password"
    defaults["is_admin"] = "is_admin"
    defaults.update(**kwargs)
    if "rank" not in defaults:
        defaults["rank"] = create_rank()
    return User.objects.create(**defaults)


def create_game(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["slug"] = "slug"
    defaults.update(**kwargs)
    return Game.objects.create(**defaults)


def create_rank(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["slug"] = "slug"
    defaults["number"] = "number"
    defaults["image"] = "image"
    defaults["description"] = "description"
    defaults["color"] = "color"
    defaults.update(**kwargs)
    return Rank.objects.create(**defaults)


def create_chapter(**kwargs):
    defaults = {}
    defaults["open_date"] = "open_date"
    defaults["launch_date"] = "launch_date"
    defaults["close_date"] = "close_date"
    defaults.update(**kwargs)
    if "members" not in defaults:
        defaults["members"] = create_user()
    if "game" not in defaults:
        defaults["game"] = create_game()
    return Chapter.objects.create(**defaults)


def create_award(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["slug"] = "slug"
    defaults["level_limit"] = "level_limit"
    defaults["order"] = "order"
    defaults["description"] = "description"
    defaults["image"] = "image"
    defaults.update(**kwargs)
    if "category" not in defaults:
        defaults["category"] = create_awardcategory()
    return Award.objects.create(**defaults)


def create_awardcategory(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["slug"] = "slug"
    defaults["order"] = "order"
    defaults.update(**kwargs)
    if "chapter" not in defaults:
        defaults["chapter"] = create_chapter()
    return AwardCategory.objects.create(**defaults)


def create_awardrecipient(**kwargs):
    defaults = {}
    defaults["reason"] = "reason"
    defaults.update(**kwargs)
    if "award" not in defaults:
        defaults["award"] = create_award()
    if "awarder" not in defaults:
        defaults["awarder"] = create_user()
    if "recipient" not in defaults:
        defaults["recipient"] = create_user()
    return AwardRecipient.objects.create(**defaults)


def create_codex(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["slug"] = "slug"
    defaults["is_article"] = "is_article"
    defaults["order"] = "order"
    defaults.update(**kwargs)
    if "parent" not in defaults:
        defaults["parent"] = create_codex()
    if "article" not in defaults:
        defaults["article"] = create_article()
    return Codex.objects.create(**defaults)


def create_article(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["slug"] = "slug"
    defaults["body"] = "body"
    defaults["body_clean"] = "body_clean"
    defaults.update(**kwargs)
    if "author" not in defaults:
        defaults["author"] = create_user()
    return Article.objects.create(**defaults)


def create_news(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "article" not in defaults:
        defaults["article"] = create_article()
    if "chapter" not in defaults:
        defaults["chapter"] = create_chapter()
    return News.objects.create(**defaults)


def create_donateamount(**kwargs):
    defaults = {}
    defaults["amount"] = "amount"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_user()
    return DonateAmount.objects.create(**defaults)


def create_donatecost(**kwargs):
    defaults = {}
    defaults["service"] = "service"
    defaults["slug"] = "slug"
    defaults["amount"] = "amount"
    defaults.update(**kwargs)
    return DonateCost.objects.create(**defaults)


def create_application(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["gender"] = "gender"
    defaults["birthdate"] = "birthdate"
    defaults["timezone"] = "timezone"
    defaults["longitude"] = "longitude"
    defaults["latitude"] = "latitude"
    defaults["character_name"] = "character_name"
    defaults["character_class"] = "character_class"
    defaults["character_level"] = "character_level"
    defaults["technical_expertise"] = "technical_expertise"
    defaults["technical_skills"] = "technical_skills"
    defaults["playtime"] = "playtime"
    defaults["player_type"] = "player_type"
    defaults["game_detailed_history"] = "game_detailed_history"
    defaults["why_join"] = "why_join"
    defaults["game_officer_history"] = "game_officer_history"
    defaults.update(**kwargs)
    if "answers" not in defaults:
        defaults["answers"] = create_applicationquestion()
    return Application.objects.create(**defaults)


def create_applicationquestion(**kwargs):
    defaults = {}
    defaults["question"] = "question"
    defaults["slug"] = "slug"
    defaults.update(**kwargs)
    if "chapter" not in defaults:
        defaults["chapter"] = create_chapter()
    return ApplicationQuestion.objects.create(**defaults)


def create_applicationanswer(**kwargs):
    defaults = {}
    defaults["answer"] = "answer"
    defaults.update(**kwargs)
    if "question" not in defaults:
        defaults["question"] = create_applicationquestion()
    return ApplicationAnswer.objects.create(**defaults)


def create_dossierguild(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["slug"] = "slug"
    defaults.update(**kwargs)
    if "game" not in defaults:
        defaults["game"] = create_game()
    return DossierGuild.objects.create(**defaults)


def create_dossierrole(**kwargs):
    defaults = {}
    defaults["role"] = "role"
    defaults["slug"] = "slug"
    defaults["duration"] = "duration"
    defaults.update(**kwargs)
    if "guild" not in defaults:
        defaults["guild"] = create_dossierguild()
    if "game" not in defaults:
        defaults["game"] = create_game()
    if "application" not in defaults:
        defaults["application"] = create_application()
    return DossierRole.objects.create(**defaults)


class UserViewTest(unittest.TestCase):
    '''
    Tests for User
    '''
    def setUp(self):
        self.client = Client()

    def test_list_user(self):
        url = reverse('backend-adt_user_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        url = reverse('backend-adt_user_create')
        data = {
            "display_name": "display_name",
            "slug": "slug",
            "email": "email",
            "signed_in": "signed_in",
            "password": "password",
            "is_admin": "is_admin",
            "rank": create_rank().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_user(self):
        user = create_user()
        url = reverse('backend-adt_user_detail', args=[user.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        user = create_user()
        data = {
            "display_name": "display_name",
            "slug": "slug",
            "email": "email",
            "signed_in": "signed_in",
            "password": "password",
            "is_admin": "is_admin",
            "rank": create_rank().id,
        }
        url = reverse('backend-adt_user_update', args=[user.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class GameViewTest(unittest.TestCase):
    '''
    Tests for Game
    '''
    def setUp(self):
        self.client = Client()

    def test_list_game(self):
        url = reverse('backend-adt_game_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_game(self):
        url = reverse('backend-adt_game_create')
        data = {
            "title": "title",
            "slug": "slug",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_game(self):
        game = create_game()
        url = reverse('backend-adt_game_detail', args=[game.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_game(self):
        game = create_game()
        data = {
            "title": "title",
            "slug": "slug",
        }
        url = reverse('backend-adt_game_update', args=[game.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RankViewTest(unittest.TestCase):
    '''
    Tests for Rank
    '''
    def setUp(self):
        self.client = Client()

    def test_list_rank(self):
        url = reverse('backend-adt_rank_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_rank(self):
        url = reverse('backend-adt_rank_create')
        data = {
            "title": "title",
            "slug": "slug",
            "number": "number",
            "image": "image",
            "description": "description",
            "color": "color",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_rank(self):
        rank = create_rank()
        url = reverse('backend-adt_rank_detail', args=[rank.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_rank(self):
        rank = create_rank()
        data = {
            "title": "title",
            "slug": "slug",
            "number": "number",
            "image": "image",
            "description": "description",
            "color": "color",
        }
        url = reverse('backend-adt_rank_update', args=[rank.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ChapterViewTest(unittest.TestCase):
    '''
    Tests for Chapter
    '''
    def setUp(self):
        self.client = Client()

    def test_list_chapter(self):
        url = reverse('backend-adt_chapter_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_chapter(self):
        url = reverse('backend-adt_chapter_create')
        data = {
            "open_date": "open_date",
            "launch_date": "launch_date",
            "close_date": "close_date",
            "members": create_user().id,
            "game": create_game().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_chapter(self):
        chapter = create_chapter()
        url = reverse('backend-adt_chapter_detail', args=[chapter.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_chapter(self):
        chapter = create_chapter()
        data = {
            "open_date": "open_date",
            "launch_date": "launch_date",
            "close_date": "close_date",
            "members": create_user().id,
            "game": create_game().id,
        }
        url = reverse('backend-adt_chapter_update', args=[chapter.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AwardViewTest(unittest.TestCase):
    '''
    Tests for Award
    '''
    def setUp(self):
        self.client = Client()

    def test_list_award(self):
        url = reverse('backend-adt_award_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_award(self):
        url = reverse('backend-adt_award_create')
        data = {
            "title": "title",
            "slug": "slug",
            "level_limit": "level_limit",
            "order": "order",
            "description": "description",
            "image": "image",
            "category": create_awardcategory().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_award(self):
        award = create_award()
        url = reverse('backend-adt_award_detail', args=[award.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_award(self):
        award = create_award()
        data = {
            "title": "title",
            "slug": "slug",
            "level_limit": "level_limit",
            "order": "order",
            "description": "description",
            "image": "image",
            "category": create_awardcategory().id,
        }
        url = reverse('backend-adt_award_update', args=[award.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AwardCategoryViewTest(unittest.TestCase):
    '''
    Tests for AwardCategory
    '''
    def setUp(self):
        self.client = Client()

    def test_list_awardcategory(self):
        url = reverse('backend-adt_awardcategory_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_awardcategory(self):
        url = reverse('backend-adt_awardcategory_create')
        data = {
            "title": "title",
            "slug": "slug",
            "order": "order",
            "chapter": create_chapter().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_awardcategory(self):
        awardcategory = create_awardcategory()
        url = reverse('backend-adt_awardcategory_detail', args=[awardcategory.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_awardcategory(self):
        awardcategory = create_awardcategory()
        data = {
            "title": "title",
            "slug": "slug",
            "order": "order",
            "chapter": create_chapter().id,
        }
        url = reverse('backend-adt_awardcategory_update', args=[awardcategory.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AwardRecipientViewTest(unittest.TestCase):
    '''
    Tests for AwardRecipient
    '''
    def setUp(self):
        self.client = Client()

    def test_list_awardrecipient(self):
        url = reverse('backend-adt_awardrecipient_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_awardrecipient(self):
        url = reverse('backend-adt_awardrecipient_create')
        data = {
            "reason": "reason",
            "award": create_award().id,
            "awarder": create_user().id,
            "recipient": create_user().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_awardrecipient(self):
        awardrecipient = create_awardrecipient()
        url = reverse('backend-adt_awardrecipient_detail', args=[awardrecipient.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_awardrecipient(self):
        awardrecipient = create_awardrecipient()
        data = {
            "reason": "reason",
            "award": create_award().id,
            "awarder": create_user().id,
            "recipient": create_user().id,
        }
        url = reverse('backend-adt_awardrecipient_update', args=[awardrecipient.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CodexViewTest(unittest.TestCase):
    '''
    Tests for Codex
    '''
    def setUp(self):
        self.client = Client()

    def test_list_codex(self):
        url = reverse('backend-adt_codex_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_codex(self):
        url = reverse('backend-adt_codex_create')
        data = {
            "title": "title",
            "slug": "slug",
            "is_article": "is_article",
            "order": "order",
            "parent": create_codex().id,
            "article": create_article().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_codex(self):
        codex = create_codex()
        url = reverse('backend-adt_codex_detail', args=[codex.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_codex(self):
        codex = create_codex()
        data = {
            "title": "title",
            "slug": "slug",
            "is_article": "is_article",
            "order": "order",
            "parent": create_codex().id,
            "article": create_article().id,
        }
        url = reverse('backend-adt_codex_update', args=[codex.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ArticleViewTest(unittest.TestCase):
    '''
    Tests for Article
    '''
    def setUp(self):
        self.client = Client()

    def test_list_article(self):
        url = reverse('backend-adt_article_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_article(self):
        url = reverse('backend-adt_article_create')
        data = {
            "title": "title",
            "slug": "slug",
            "body": "body",
            "body_clean": "body_clean",
            "author": create_user().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_article(self):
        article = create_article()
        url = reverse('backend-adt_article_detail', args=[article.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_article(self):
        article = create_article()
        data = {
            "title": "title",
            "slug": "slug",
            "body": "body",
            "body_clean": "body_clean",
            "author": create_user().id,
        }
        url = reverse('backend-adt_article_update', args=[article.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class NewsViewTest(unittest.TestCase):
    '''
    Tests for News
    '''
    def setUp(self):
        self.client = Client()

    def test_list_news(self):
        url = reverse('backend-adt_news_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_news(self):
        url = reverse('backend-adt_news_create')
        data = {
            "article": create_article().id,
            "chapter": create_chapter().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_news(self):
        news = create_news()
        url = reverse('backend-adt_news_detail', args=[news.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_news(self):
        news = create_news()
        data = {
            "article": create_article().id,
            "chapter": create_chapter().id,
        }
        url = reverse('backend-adt_news_update', args=[news.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DonateAmountViewTest(unittest.TestCase):
    '''
    Tests for DonateAmount
    '''
    def setUp(self):
        self.client = Client()

    def test_list_donateamount(self):
        url = reverse('backend-adt_donateamount_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_donateamount(self):
        url = reverse('backend-adt_donateamount_create')
        data = {
            "amount": "amount",
            "user": create_user().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_donateamount(self):
        donateamount = create_donateamount()
        url = reverse('backend-adt_donateamount_detail', args=[donateamount.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_donateamount(self):
        donateamount = create_donateamount()
        data = {
            "amount": "amount",
            "user": create_user().id,
        }
        url = reverse('backend-adt_donateamount_update', args=[donateamount.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DonateCostViewTest(unittest.TestCase):
    '''
    Tests for DonateCost
    '''
    def setUp(self):
        self.client = Client()

    def test_list_donatecost(self):
        url = reverse('backend-adt_donatecost_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_donatecost(self):
        url = reverse('backend-adt_donatecost_create')
        data = {
            "service": "service",
            "slug": "slug",
            "amount": "amount",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_donatecost(self):
        donatecost = create_donatecost()
        url = reverse('backend-adt_donatecost_detail', args=[donatecost.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_donatecost(self):
        donatecost = create_donatecost()
        data = {
            "service": "service",
            "slug": "slug",
            "amount": "amount",
        }
        url = reverse('backend-adt_donatecost_update', args=[donatecost.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ApplicationViewTest(unittest.TestCase):
    '''
    Tests for Application
    '''
    def setUp(self):
        self.client = Client()

    def test_list_application(self):
        url = reverse('backend-adt_application_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_application(self):
        url = reverse('backend-adt_application_create')
        data = {
            "name": "name",
            "gender": "gender",
            "birthdate": "birthdate",
            "timezone": "timezone",
            "longitude": "longitude",
            "latitude": "latitude",
            "character_name": "character_name",
            "character_class": "character_class",
            "character_level": "character_level",
            "technical_expertise": "technical_expertise",
            "technical_skills": "technical_skills",
            "playtime": "playtime",
            "player_type": "player_type",
            "game_detailed_history": "game_detailed_history",
            "why_join": "why_join",
            "game_officer_history": "game_officer_history",
            "answers": create_applicationquestion().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_application(self):
        application = create_application()
        url = reverse('backend-adt_application_detail', args=[application.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_application(self):
        application = create_application()
        data = {
            "name": "name",
            "gender": "gender",
            "birthdate": "birthdate",
            "timezone": "timezone",
            "longitude": "longitude",
            "latitude": "latitude",
            "character_name": "character_name",
            "character_class": "character_class",
            "character_level": "character_level",
            "technical_expertise": "technical_expertise",
            "technical_skills": "technical_skills",
            "playtime": "playtime",
            "player_type": "player_type",
            "game_detailed_history": "game_detailed_history",
            "why_join": "why_join",
            "game_officer_history": "game_officer_history",
            "answers": create_applicationquestion().id,
        }
        url = reverse('backend-adt_application_update', args=[application.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ApplicationQuestionViewTest(unittest.TestCase):
    '''
    Tests for ApplicationQuestion
    '''
    def setUp(self):
        self.client = Client()

    def test_list_applicationquestion(self):
        url = reverse('backend-adt_applicationquestion_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_applicationquestion(self):
        url = reverse('backend-adt_applicationquestion_create')
        data = {
            "question": "question",
            "slug": "slug",
            "chapter": create_chapter().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_applicationquestion(self):
        applicationquestion = create_applicationquestion()
        url = reverse('backend-adt_applicationquestion_detail', args=[applicationquestion.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_applicationquestion(self):
        applicationquestion = create_applicationquestion()
        data = {
            "question": "question",
            "slug": "slug",
            "chapter": create_chapter().id,
        }
        url = reverse('backend-adt_applicationquestion_update', args=[applicationquestion.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ApplicationAnswerViewTest(unittest.TestCase):
    '''
    Tests for ApplicationAnswer
    '''
    def setUp(self):
        self.client = Client()

    def test_list_applicationanswer(self):
        url = reverse('backend-adt_applicationanswer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_applicationanswer(self):
        url = reverse('backend-adt_applicationanswer_create')
        data = {
            "answer": "answer",
            "question": create_applicationquestion().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_applicationanswer(self):
        applicationanswer = create_applicationanswer()
        url = reverse('backend-adt_applicationanswer_detail', args=[applicationanswer.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_applicationanswer(self):
        applicationanswer = create_applicationanswer()
        data = {
            "answer": "answer",
            "question": create_applicationquestion().id,
        }
        url = reverse('backend-adt_applicationanswer_update', args=[applicationanswer.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DossierGuildViewTest(unittest.TestCase):
    '''
    Tests for DossierGuild
    '''
    def setUp(self):
        self.client = Client()

    def test_list_dossierguild(self):
        url = reverse('backend-adt_dossierguild_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_dossierguild(self):
        url = reverse('backend-adt_dossierguild_create')
        data = {
            "title": "title",
            "slug": "slug",
            "game": create_game().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_dossierguild(self):
        dossierguild = create_dossierguild()
        url = reverse('backend-adt_dossierguild_detail', args=[dossierguild.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_dossierguild(self):
        dossierguild = create_dossierguild()
        data = {
            "title": "title",
            "slug": "slug",
            "game": create_game().id,
        }
        url = reverse('backend-adt_dossierguild_update', args=[dossierguild.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DossierRoleViewTest(unittest.TestCase):
    '''
    Tests for DossierRole
    '''
    def setUp(self):
        self.client = Client()

    def test_list_dossierrole(self):
        url = reverse('backend-adt_dossierrole_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_dossierrole(self):
        url = reverse('backend-adt_dossierrole_create')
        data = {
            "role": "role",
            "slug": "slug",
            "duration": "duration",
            "guild": create_dossierguild().id,
            "game": create_game().id,
            "application": create_application().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_dossierrole(self):
        dossierrole = create_dossierrole()
        url = reverse('backend-adt_dossierrole_detail', args=[dossierrole.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_dossierrole(self):
        dossierrole = create_dossierrole()
        data = {
            "role": "role",
            "slug": "slug",
            "duration": "duration",
            "guild": create_dossierguild().id,
            "game": create_game().id,
            "application": create_application().id,
        }
        url = reverse('backend-adt_dossierrole_update', args=[dossierrole.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


