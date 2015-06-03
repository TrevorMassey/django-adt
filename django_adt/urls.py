from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from games.api import GameViewSet, ChapterViewSet
from awards.api import AwardViewSet, AwardCategoryViewSet, AwardRecipientViewSet, AwardImageViewSet
from users.api import RankViewSet
from publications.api import ArticleViewSet, NewsViewSet
from accounting.api import DonateCostViewSet, DonateAmountViewSet
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'frontend.views.spa', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

router = DefaultRouter()

router.register(r'games', GameViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'awards', AwardViewSet)
router.register(r'awards-categories', AwardCategoryViewSet)
router.register(r'awards-recipients', AwardRecipientViewSet)
router.register(r'awards-images', AwardImageViewSet)
router.register(r'ranks', RankViewSet)
router.register(r'donation-costs', DonateCostViewSet)
router.register(r'donation-amounts', DonateAmountViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'news', NewsViewSet)

urlpatterns += patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^api/awards-summary/$', 'awards.api.awards_summary', name='awards_summary'),
    url(r'^api/codex/$', 'publications.api.codex_list', name='codex_list'),
    url(r'^api/codex/(?P<pk>\d+)/$', 'publications.api.codex_detail', name='codex_detail'),

    url(r'^api/users/register/$', 'users.api.user_registration', name='user_registration'),
    url(r'^api/users/profile/$', 'users.api.user_profile', name='user_profile'),

    url(r'^verify/(?P<key>[A-Za-z0-9]{32})/$', 'users.views.verify_email', name='verify_email'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
