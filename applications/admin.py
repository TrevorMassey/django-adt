from django.contrib import admin
from django import forms
#
#
# class UserAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = User
#
#
# class UserAdmin(admin.ModelAdmin):
#     form = UserAdminForm
#     list_display = ['display_name', 'slug', 'created', 'email', 'signed_in', 'last_active', 'password', 'is_admin']
#     readonly_fields = ['display_name', 'slug', 'created', 'email', 'signed_in', 'last_active', 'password', 'is_admin']
#
# admin.site.register(User, UserAdmin)
#
#
# class GameAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = Game
#
#
# class GameAdmin(admin.ModelAdmin):
#     form = GameAdminForm
#     list_display = ['title', 'slug']
#     readonly_fields = ['title', 'slug']
#
# admin.site.register(Game, GameAdmin)
#
#
# class RankAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = Rank
#
#
# class RankAdmin(admin.ModelAdmin):
#     form = RankAdminForm
#     list_display = ['title', 'slug', 'number', 'image', 'description', 'color']
#     readonly_fields = ['title', 'slug', 'number', 'image', 'description', 'color']
#
# admin.site.register(Rank, RankAdmin)
#
#
# class ChapterAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = Chapter
#
#
# class ChapterAdmin(admin.ModelAdmin):
#     form = ChapterAdminForm
#     list_display = ['open_date', 'launch_date', 'close_date']
#     readonly_fields = ['open_date', 'launch_date', 'close_date']
#
# admin.site.register(Chapter, ChapterAdmin)
#
#
# class AwardAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = Award
#
#
# class AwardAdmin(admin.ModelAdmin):
#     form = AwardAdminForm
#     list_display = ['title', 'slug', 'level_limit', 'order', 'description', 'image']
#     readonly_fields = ['title', 'slug', 'level_limit', 'order', 'description', 'image']
#
# admin.site.register(Award, AwardAdmin)
#
#
# class AwardCategoryAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = AwardCategory
#
#
# class AwardCategoryAdmin(admin.ModelAdmin):
#     form = AwardCategoryAdminForm
#     list_display = ['title', 'slug', 'order']
#     readonly_fields = ['title', 'slug', 'order']
#
# admin.site.register(AwardCategory, AwardCategoryAdmin)
#
#
# class AwardRecipientAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = AwardRecipient
#
#
# class AwardRecipientAdmin(admin.ModelAdmin):
#     form = AwardRecipientAdminForm
#     list_display = ['reason', 'created']
#     readonly_fields = ['reason', 'created']
#
# admin.site.register(AwardRecipient, AwardRecipientAdmin)
#
#
# class CodexAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = Codex
#
#
# class CodexAdmin(admin.ModelAdmin):
#     form = CodexAdminForm
#     list_display = ['title', 'slug', 'created', 'last_updated', 'is_article', 'order']
#     readonly_fields = ['title', 'slug', 'created', 'last_updated', 'is_article', 'order']
#
# admin.site.register(Codex, CodexAdmin)
#
#
# class ArticleAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = Article
#
#
# class ArticleAdmin(admin.ModelAdmin):
#     form = ArticleAdminForm
#     list_display = ['title', 'slug', 'created', 'last_updated', 'body', 'body_clean']
#     readonly_fields = ['title', 'slug', 'created', 'last_updated', 'body', 'body_clean']
#
# admin.site.register(Article, ArticleAdmin)
#
#
# class NewsAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = News
#
#
# class NewsAdmin(admin.ModelAdmin):
#     form = NewsAdminForm
#     list_display = ['']
#     readonly_fields = ['']
#
# admin.site.register(News, NewsAdmin)
#
#
# class DonateAmountAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = DonateAmount
#
#
# class DonateAmountAdmin(admin.ModelAdmin):
#     form = DonateAmountAdminForm
#     list_display = ['created', 'amount']
#     readonly_fields = ['created', 'amount']
#
# admin.site.register(DonateAmount, DonateAmountAdmin)
#
#
# class DonateCostAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = DonateCost
#
#
# class DonateCostAdmin(admin.ModelAdmin):
#     form = DonateCostAdminForm
#     list_display = ['service', 'slug', 'created', 'last_updated', 'amount']
#     readonly_fields = ['service', 'slug', 'created', 'last_updated', 'amount']
#
# admin.site.register(DonateCost, DonateCostAdmin)
#
#
# class ApplicationAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = Application
#
#
# class ApplicationAdmin(admin.ModelAdmin):
#     form = ApplicationAdminForm
#     list_display = ['created', 'last_updated', 'name', 'gender', 'birthdate', 'timezone', 'longitude', 'latitude', 'character_name', 'character_class', 'character_level', 'technical_expertise', 'technical_skills', 'playtime', 'player_type', 'game_detailed_history', 'why_join', 'game_officer_history']
#     readonly_fields = ['created', 'last_updated', 'name', 'gender', 'birthdate', 'timezone', 'longitude', 'latitude', 'character_name', 'character_class', 'character_level', 'technical_expertise', 'technical_skills', 'playtime', 'player_type', 'game_detailed_history', 'why_join', 'game_officer_history']
#
# admin.site.register(Application, ApplicationAdmin)
#
#
# class ApplicationQuestionAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = ApplicationQuestion
#
#
# class ApplicationQuestionAdmin(admin.ModelAdmin):
#     form = ApplicationQuestionAdminForm
#     list_display = ['question', 'slug', 'created', 'last_updated']
#     readonly_fields = ['question', 'slug', 'created', 'last_updated']
#
# admin.site.register(ApplicationQuestion, ApplicationQuestionAdmin)
#
#
# class ApplicationAnswerAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = ApplicationAnswer
#
#
# class ApplicationAnswerAdmin(admin.ModelAdmin):
#     form = ApplicationAnswerAdminForm
#     list_display = ['answer', 'created']
#     readonly_fields = ['answer', 'created']
#
# admin.site.register(ApplicationAnswer, ApplicationAnswerAdmin)
#
#
# class DossierGuildAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = DossierGuild
#
#
# class DossierGuildAdmin(admin.ModelAdmin):
#     form = DossierGuildAdminForm
#     list_display = ['title', 'slug', 'created']
#     readonly_fields = ['title', 'slug', 'created']
#
# admin.site.register(DossierGuild, DossierGuildAdmin)
#
#
# class DossierRoleAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = DossierRole
#
#
# class DossierRoleAdmin(admin.ModelAdmin):
#     form = DossierRoleAdminForm
#     list_display = ['role', 'slug', 'created', 'duration']
#     readonly_fields = ['role', 'slug', 'created', 'duration']
#
# admin.site.register(DossierRole, DossierRoleAdmin)
#
#
