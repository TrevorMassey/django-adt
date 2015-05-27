from django.conf.urls import patterns, url
from .views import UserListView, GameListView, RankListView, ChapterListView, AwardListView, AwardCategoryListView, AwardRecipientListView, CodexListView, ArticleListView, NewsListView, DonateAmountListView, DonateCostListView, ApplicationListView, ApplicationQuestionListView, ApplicationAnswerListView, DossierGuildListView, DossierRoleListView
from .views import UserDetailView, GameDetailView, RankDetailView, ChapterDetailView, AwardDetailView, AwardCategoryDetailView, AwardRecipientDetailView, CodexDetailView, ArticleDetailView, NewsDetailView, DonateAmountDetailView, DonateCostDetailView, ApplicationDetailView, ApplicationQuestionDetailView, ApplicationAnswerDetailView, DossierGuildDetailView, DossierRoleDetailView
from .views import UserCreateView, GameCreateView, RankCreateView, ChapterCreateView, AwardCreateView, AwardCategoryCreateView, AwardRecipientCreateView, CodexCreateView, ArticleCreateView, NewsCreateView, DonateAmountCreateView, DonateCostCreateView, ApplicationCreateView, ApplicationQuestionCreateView, ApplicationAnswerCreateView, DossierGuildCreateView, DossierRoleCreateView
from .views import UserUpdateView, GameUpdateView, RankUpdateView, ChapterUpdateView, AwardUpdateView, AwardCategoryUpdateView, AwardRecipientUpdateView, CodexUpdateView, ArticleUpdateView, NewsUpdateView, DonateAmountUpdateView, DonateCostUpdateView, ApplicationUpdateView, ApplicationQuestionUpdateView, ApplicationAnswerUpdateView, DossierGuildUpdateView, DossierRoleUpdateView

urlpatterns = patterns('')

urlpatterns += patterns('',
    # urls for User
    url(r'^backend-adt/user/$', UserListView.as_view(), name='backend-adt_user_list'),
    url(r'^backend-adt/user/create/$', UserCreateView.as_view(), name='backend-adt_user_create'),
    url(r'^backend-adt/user/detail/(?P<slug>\S+)/$', UserDetailView.as_view(), name='backend-adt_user_detail'),
    url(r'^backend-adt/user/update/(?P<slug>\S+)/$', UserUpdateView.as_view(), name='backend-adt_user_update'),
)

urlpatterns += patterns('',
    # urls for Game
    url(r'^backend-adt/game/$', GameListView.as_view(), name='backend-adt_game_list'),
    url(r'^backend-adt/game/create/$', GameCreateView.as_view(), name='backend-adt_game_create'),
    url(r'^backend-adt/game/detail/(?P<slug>\S+)/$', GameDetailView.as_view(), name='backend-adt_game_detail'),
    url(r'^backend-adt/game/update/(?P<slug>\S+)/$', GameUpdateView.as_view(), name='backend-adt_game_update'),
)

urlpatterns += patterns('',
    # urls for Rank
    url(r'^backend-adt/rank/$', RankListView.as_view(), name='backend-adt_rank_list'),
    url(r'^backend-adt/rank/create/$', RankCreateView.as_view(), name='backend-adt_rank_create'),
    url(r'^backend-adt/rank/detail/(?P<slug>\S+)/$', RankDetailView.as_view(), name='backend-adt_rank_detail'),
    url(r'^backend-adt/rank/update/(?P<slug>\S+)/$', RankUpdateView.as_view(), name='backend-adt_rank_update'),
)

urlpatterns += patterns('',
    # urls for Chapter
    url(r'^backend-adt/chapter/$', ChapterListView.as_view(), name='backend-adt_chapter_list'),
    url(r'^backend-adt/chapter/create/$', ChapterCreateView.as_view(), name='backend-adt_chapter_create'),
    url(r'^backend-adt/chapter/detail/(?P<id>\S+)/$', ChapterDetailView.as_view(), name='backend-adt_chapter_detail'),
    url(r'^backend-adt/chapter/update/(?P<id>\S+)/$', ChapterUpdateView.as_view(), name='backend-adt_chapter_update'),
)

urlpatterns += patterns('',
    # urls for Award
    url(r'^backend-adt/award/$', AwardListView.as_view(), name='backend-adt_award_list'),
    url(r'^backend-adt/award/create/$', AwardCreateView.as_view(), name='backend-adt_award_create'),
    url(r'^backend-adt/award/detail/(?P<slug>\S+)/$', AwardDetailView.as_view(), name='backend-adt_award_detail'),
    url(r'^backend-adt/award/update/(?P<slug>\S+)/$', AwardUpdateView.as_view(), name='backend-adt_award_update'),
)

urlpatterns += patterns('',
    # urls for AwardCategory
    url(r'^backend-adt/awardcategory/$', AwardCategoryListView.as_view(), name='backend-adt_awardcategory_list'),
    url(r'^backend-adt/awardcategory/create/$', AwardCategoryCreateView.as_view(), name='backend-adt_awardcategory_create'),
    url(r'^backend-adt/awardcategory/detail/(?P<slug>\S+)/$', AwardCategoryDetailView.as_view(), name='backend-adt_awardcategory_detail'),
    url(r'^backend-adt/awardcategory/update/(?P<slug>\S+)/$', AwardCategoryUpdateView.as_view(), name='backend-adt_awardcategory_update'),
)

urlpatterns += patterns('',
    # urls for AwardRecipient
    url(r'^backend-adt/awardrecipient/$', AwardRecipientListView.as_view(), name='backend-adt_awardrecipient_list'),
    url(r'^backend-adt/awardrecipient/create/$', AwardRecipientCreateView.as_view(), name='backend-adt_awardrecipient_create'),
    url(r'^backend-adt/awardrecipient/detail/(?P<id>\S+)/$', AwardRecipientDetailView.as_view(), name='backend-adt_awardrecipient_detail'),
    url(r'^backend-adt/awardrecipient/update/(?P<id>\S+)/$', AwardRecipientUpdateView.as_view(), name='backend-adt_awardrecipient_update'),
)

urlpatterns += patterns('',
    # urls for Codex
    url(r'^backend-adt/codex/$', CodexListView.as_view(), name='backend-adt_codex_list'),
    url(r'^backend-adt/codex/create/$', CodexCreateView.as_view(), name='backend-adt_codex_create'),
    url(r'^backend-adt/codex/detail/(?P<slug>\S+)/$', CodexDetailView.as_view(), name='backend-adt_codex_detail'),
    url(r'^backend-adt/codex/update/(?P<slug>\S+)/$', CodexUpdateView.as_view(), name='backend-adt_codex_update'),
)

urlpatterns += patterns('',
    # urls for Article
    url(r'^backend-adt/article/$', ArticleListView.as_view(), name='backend-adt_article_list'),
    url(r'^backend-adt/article/create/$', ArticleCreateView.as_view(), name='backend-adt_article_create'),
    url(r'^backend-adt/article/detail/(?P<slug>\S+)/$', ArticleDetailView.as_view(), name='backend-adt_article_detail'),
    url(r'^backend-adt/article/update/(?P<slug>\S+)/$', ArticleUpdateView.as_view(), name='backend-adt_article_update'),
)

urlpatterns += patterns('',
    # urls for News
    url(r'^backend-adt/news/$', NewsListView.as_view(), name='backend-adt_news_list'),
    url(r'^backend-adt/news/create/$', NewsCreateView.as_view(), name='backend-adt_news_create'),
    url(r'^backend-adt/news/detail/(?P<id>\S+)/$', NewsDetailView.as_view(), name='backend-adt_news_detail'),
    url(r'^backend-adt/news/update/(?P<id>\S+)/$', NewsUpdateView.as_view(), name='backend-adt_news_update'),
)

urlpatterns += patterns('',
    # urls for DonateAmount
    url(r'^backend-adt/donateamount/$', DonateAmountListView.as_view(), name='backend-adt_donateamount_list'),
    url(r'^backend-adt/donateamount/create/$', DonateAmountCreateView.as_view(), name='backend-adt_donateamount_create'),
    url(r'^backend-adt/donateamount/detail/(?P<id>\S+)/$', DonateAmountDetailView.as_view(), name='backend-adt_donateamount_detail'),
    url(r'^backend-adt/donateamount/update/(?P<id>\S+)/$', DonateAmountUpdateView.as_view(), name='backend-adt_donateamount_update'),
)

urlpatterns += patterns('',
    # urls for DonateCost
    url(r'^backend-adt/donatecost/$', DonateCostListView.as_view(), name='backend-adt_donatecost_list'),
    url(r'^backend-adt/donatecost/create/$', DonateCostCreateView.as_view(), name='backend-adt_donatecost_create'),
    url(r'^backend-adt/donatecost/detail/(?P<slug>\S+)/$', DonateCostDetailView.as_view(), name='backend-adt_donatecost_detail'),
    url(r'^backend-adt/donatecost/update/(?P<slug>\S+)/$', DonateCostUpdateView.as_view(), name='backend-adt_donatecost_update'),
)

urlpatterns += patterns('',
    # urls for Application
    url(r'^backend-adt/application/$', ApplicationListView.as_view(), name='backend-adt_application_list'),
    url(r'^backend-adt/application/create/$', ApplicationCreateView.as_view(), name='backend-adt_application_create'),
    url(r'^backend-adt/application/detail/(?P<id>\S+)/$', ApplicationDetailView.as_view(), name='backend-adt_application_detail'),
    url(r'^backend-adt/application/update/(?P<id>\S+)/$', ApplicationUpdateView.as_view(), name='backend-adt_application_update'),
)

urlpatterns += patterns('',
    # urls for ApplicationQuestion
    url(r'^backend-adt/applicationquestion/$', ApplicationQuestionListView.as_view(), name='backend-adt_applicationquestion_list'),
    url(r'^backend-adt/applicationquestion/create/$', ApplicationQuestionCreateView.as_view(), name='backend-adt_applicationquestion_create'),
    url(r'^backend-adt/applicationquestion/detail/(?P<slug>\S+)/$', ApplicationQuestionDetailView.as_view(), name='backend-adt_applicationquestion_detail'),
    url(r'^backend-adt/applicationquestion/update/(?P<slug>\S+)/$', ApplicationQuestionUpdateView.as_view(), name='backend-adt_applicationquestion_update'),
)

urlpatterns += patterns('',
    # urls for ApplicationAnswer
    url(r'^backend-adt/applicationanswer/$', ApplicationAnswerListView.as_view(), name='backend-adt_applicationanswer_list'),
    url(r'^backend-adt/applicationanswer/create/$', ApplicationAnswerCreateView.as_view(), name='backend-adt_applicationanswer_create'),
    url(r'^backend-adt/applicationanswer/detail/(?P<id>\S+)/$', ApplicationAnswerDetailView.as_view(), name='backend-adt_applicationanswer_detail'),
    url(r'^backend-adt/applicationanswer/update/(?P<id>\S+)/$', ApplicationAnswerUpdateView.as_view(), name='backend-adt_applicationanswer_update'),
)

urlpatterns += patterns('',
    # urls for DossierGuild
    url(r'^backend-adt/dossierguild/$', DossierGuildListView.as_view(), name='backend-adt_dossierguild_list'),
    url(r'^backend-adt/dossierguild/create/$', DossierGuildCreateView.as_view(), name='backend-adt_dossierguild_create'),
    url(r'^backend-adt/dossierguild/detail/(?P<slug>\S+)/$', DossierGuildDetailView.as_view(), name='backend-adt_dossierguild_detail'),
    url(r'^backend-adt/dossierguild/update/(?P<slug>\S+)/$', DossierGuildUpdateView.as_view(), name='backend-adt_dossierguild_update'),
)

urlpatterns += patterns('',
    # urls for DossierRole
    url(r'^backend-adt/dossierrole/$', DossierRoleListView.as_view(), name='backend-adt_dossierrole_list'),
    url(r'^backend-adt/dossierrole/create/$', DossierRoleCreateView.as_view(), name='backend-adt_dossierrole_create'),
    url(r'^backend-adt/dossierrole/detail/(?P<slug>\S+)/$', DossierRoleDetailView.as_view(), name='backend-adt_dossierrole_detail'),
    url(r'^backend-adt/dossierrole/update/(?P<slug>\S+)/$', DossierRoleUpdateView.as_view(), name='backend-adt_dossierrole_update'),
)

