from django.conf.urls import patterns, include, url
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
    # url(r'^$', 'django_adt.views.home', name='home'),
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
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
