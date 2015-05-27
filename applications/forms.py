from django import forms
from .models import User, Game, Rank, Chapter, Award, AwardCategory, AwardRecipient, Codex, Article, News, DonateAmount, DonateCost, Application, ApplicationQuestion, ApplicationAnswer, DossierGuild, DossierRole


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['display_name', 'slug', 'email', 'signed_in', 'password', 'is_admin', 'rank']


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'slug']


class RankForm(forms.ModelForm):
    class Meta:
        model = Rank
        fields = ['title', 'slug', 'number', 'image', 'description', 'color']


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['open_date', 'launch_date', 'close_date', 'user', 'game']


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['title', 'slug', 'level_limit', 'order', 'description', 'image', 'awardcategory']


class AwardCategoryForm(forms.ModelForm):
    class Meta:
        model = AwardCategory
        fields = ['title', 'slug', 'order', 'chapter']


class AwardRecipientForm(forms.ModelForm):
    class Meta:
        model = AwardRecipient
        fields = ['reason', 'award', 'user', 'user']


class CodexForm(forms.ModelForm):
    class Meta:
        model = Codex
        fields = ['title', 'slug', 'is_article', 'order', 'codex', 'article']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'body', 'body_clean', 'user']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['article', 'chapter']


class DonateAmountForm(forms.ModelForm):
    class Meta:
        model = DonateAmount
        fields = ['amount', 'user']


class DonateCostForm(forms.ModelForm):
    class Meta:
        model = DonateCost
        fields = ['service', 'slug', 'amount']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'gender', 'birthdate', 'timezone', 'longitude', 'latitude', 'character_name', 'character_class', 'character_level', 'technical_expertise', 'technical_skills', 'playtime', 'player_type', 'game_detailed_history', 'why_join', 'game_officer_history', 'applicationquestion']


class ApplicationQuestionForm(forms.ModelForm):
    class Meta:
        model = ApplicationQuestion
        fields = ['question', 'slug', 'chapter']


class ApplicationAnswerForm(forms.ModelForm):
    class Meta:
        model = ApplicationAnswer
        fields = ['answer', 'applicationquestion']


class DossierGuildForm(forms.ModelForm):
    class Meta:
        model = DossierGuild
        fields = ['title', 'slug', 'game']


class DossierRoleForm(forms.ModelForm):
    class Meta:
        model = DossierRole
        fields = ['role', 'slug', 'duration', 'dossierguild', 'game', 'application']


