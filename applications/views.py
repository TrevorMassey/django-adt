from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import User, Game, Rank, Chapter, Award, AwardCategory, AwardRecipient, Codex, Article, News, DonateAmount, DonateCost, Application, ApplicationQuestion, ApplicationAnswer, DossierGuild, DossierRole
from .forms import UserForm, GameForm, RankForm, ChapterForm, AwardForm, AwardCategoryForm, AwardRecipientForm, CodexForm, ArticleForm, NewsForm, DonateAmountForm, DonateCostForm, ApplicationForm, ApplicationQuestionForm, ApplicationAnswerForm, DossierGuildForm, DossierRoleForm


class UserListView(ListView):
    model = User


class UserCreateView(CreateView):
    model = User
    form_class = UserForm


class UserDetailView(DetailView):
    model = User


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm


class GameListView(ListView):
    model = Game


class GameCreateView(CreateView):
    model = Game
    form_class = GameForm


class GameDetailView(DetailView):
    model = Game


class GameUpdateView(UpdateView):
    model = Game
    form_class = GameForm


class RankListView(ListView):
    model = Rank


class RankCreateView(CreateView):
    model = Rank
    form_class = RankForm


class RankDetailView(DetailView):
    model = Rank


class RankUpdateView(UpdateView):
    model = Rank
    form_class = RankForm


class ChapterListView(ListView):
    model = Chapter


class ChapterCreateView(CreateView):
    model = Chapter
    form_class = ChapterForm


class ChapterDetailView(DetailView):
    model = Chapter


class ChapterUpdateView(UpdateView):
    model = Chapter
    form_class = ChapterForm


class AwardListView(ListView):
    model = Award


class AwardCreateView(CreateView):
    model = Award
    form_class = AwardForm


class AwardDetailView(DetailView):
    model = Award


class AwardUpdateView(UpdateView):
    model = Award
    form_class = AwardForm


class AwardCategoryListView(ListView):
    model = AwardCategory


class AwardCategoryCreateView(CreateView):
    model = AwardCategory
    form_class = AwardCategoryForm


class AwardCategoryDetailView(DetailView):
    model = AwardCategory


class AwardCategoryUpdateView(UpdateView):
    model = AwardCategory
    form_class = AwardCategoryForm


class AwardRecipientListView(ListView):
    model = AwardRecipient


class AwardRecipientCreateView(CreateView):
    model = AwardRecipient
    form_class = AwardRecipientForm


class AwardRecipientDetailView(DetailView):
    model = AwardRecipient


class AwardRecipientUpdateView(UpdateView):
    model = AwardRecipient
    form_class = AwardRecipientForm


class CodexListView(ListView):
    model = Codex


class CodexCreateView(CreateView):
    model = Codex
    form_class = CodexForm


class CodexDetailView(DetailView):
    model = Codex


class CodexUpdateView(UpdateView):
    model = Codex
    form_class = CodexForm


class ArticleListView(ListView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm


class ArticleDetailView(DetailView):
    model = Article


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm


class NewsListView(ListView):
    model = News


class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm


class NewsDetailView(DetailView):
    model = News


class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm


class DonateAmountListView(ListView):
    model = DonateAmount


class DonateAmountCreateView(CreateView):
    model = DonateAmount
    form_class = DonateAmountForm


class DonateAmountDetailView(DetailView):
    model = DonateAmount


class DonateAmountUpdateView(UpdateView):
    model = DonateAmount
    form_class = DonateAmountForm


class DonateCostListView(ListView):
    model = DonateCost


class DonateCostCreateView(CreateView):
    model = DonateCost
    form_class = DonateCostForm


class DonateCostDetailView(DetailView):
    model = DonateCost


class DonateCostUpdateView(UpdateView):
    model = DonateCost
    form_class = DonateCostForm


class ApplicationListView(ListView):
    model = Application


class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationForm


class ApplicationDetailView(DetailView):
    model = Application


class ApplicationUpdateView(UpdateView):
    model = Application
    form_class = ApplicationForm


class ApplicationQuestionListView(ListView):
    model = ApplicationQuestion


class ApplicationQuestionCreateView(CreateView):
    model = ApplicationQuestion
    form_class = ApplicationQuestionForm


class ApplicationQuestionDetailView(DetailView):
    model = ApplicationQuestion


class ApplicationQuestionUpdateView(UpdateView):
    model = ApplicationQuestion
    form_class = ApplicationQuestionForm


class ApplicationAnswerListView(ListView):
    model = ApplicationAnswer


class ApplicationAnswerCreateView(CreateView):
    model = ApplicationAnswer
    form_class = ApplicationAnswerForm


class ApplicationAnswerDetailView(DetailView):
    model = ApplicationAnswer


class ApplicationAnswerUpdateView(UpdateView):
    model = ApplicationAnswer
    form_class = ApplicationAnswerForm


class DossierGuildListView(ListView):
    model = DossierGuild


class DossierGuildCreateView(CreateView):
    model = DossierGuild
    form_class = DossierGuildForm


class DossierGuildDetailView(DetailView):
    model = DossierGuild


class DossierGuildUpdateView(UpdateView):
    model = DossierGuild
    form_class = DossierGuildForm


class DossierRoleListView(ListView):
    model = DossierRole


class DossierRoleCreateView(CreateView):
    model = DossierRole
    form_class = DossierRoleForm


class DossierRoleDetailView(DetailView):
    model = DossierRole


class DossierRoleUpdateView(UpdateView):
    model = DossierRole
    form_class = DossierRoleForm

