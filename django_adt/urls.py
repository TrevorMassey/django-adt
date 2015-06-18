from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^$', 'frontend.views.index', name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       )

router = DefaultRouter()


urlpatterns += patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),

    # Awards
    url(r'^api/awards/$', 'awards.api.award_list', name='award_list'),
    url(r'^api/awards/(?P<slug>[a-z0-9-]+)/$', 'awards.api.award_detail', name='award_detail'),
    url(r'^api/awards/(?P<slug>[a-z0-9-]+)/recipients/$', 'awards.api.award_recipient_list', name='award_recipient_list'),
    url(r'^api/awards/(?P<slug>[a-z0-9-]+)/recipients/(?P<pk>\d+)/$', 'awards.api.award_recipient_detail', name='award_recipient_detail'),
    url(r'^api/award-images/$', 'awards.api.award_image_list', name='award_image_list'),
    url(r'^api/award-images/(?P<slug>[a-z0-9-]+)/$', 'awards.api.award_image_detail', name='award_image_detail'),
    # Categories could be nested under chapter
    url(r'^api/award-categories/$', 'awards.api.award_category_list', name='award_category_list'),
    url(r'^api/award-categories/(?P<slug>[a-z0-9-]+)/$', 'awards.api.award_category_detail', name='award_category_detail'),
    url(r'^api/awards-summary/$', 'awards.api.awards_summary', name='awards_summary'),

    # Donations
    url(r'^api/donations/$', 'accounting.api.donate_list', name='donation_list'),
    url(r'^api/donations/(?P<pk>\d+)/$', 'accounting.api.donate_detail', name='donation_detail'),
    url(r'^api/donation-costs/$', 'accounting.api.cost_list', name='cost_list'),
    url(r'^api/donation-costs/(?P<pk>\d+)/$', 'accounting.api.cost_detail', name='cost_detail'),
    url(r'^api/donation-goals/$', 'accounting.api.goal_list', name='goal_list'),
    url(r'^api/donation-goals/(?P<pk>\d+)/$', 'accounting.api.goal_detail', name='goal_detail'),

    # Games
    url(r'^api/games/$', 'games.api.game_list', name='game_list'),
    url(r'^api/games/(?P<slug>[a-z0-9-]+)/$', 'games.api.game_detail', name='game_detail'),
    url(r'^api/guilds/$', 'games.api.game_list', name='game_list'),
    url(r'^api/guilds/(?P<slug>[a-z0-9-]+)/$', 'games.api.game_detail', name='game_detail'),

    # TODO this needs to be updated to slugs - not sure how to create slug for chapter
    url(r'^api/chapters/$', 'games.api.chapter_list', name='chapter_list'),
    url(r'^api/chapters/(?P<pk>\d+)/$', 'games.api.chapter_detail', name='chapter_detail'),
    url(r'^api/chapters/(?P<pk>\d+)/divisions/$', 'games.api.chapter_division_list', name='chapter_division_list'),
    url(r'^api/chapters/(?P<pk>\d+)/divisions/(?P<slug>[a-z0-9-]+)/$', 'games.api.chapter_division_detail', name='chapter_division_detail'),
    url(r'^api/chapters/(?P<pk>\d+)/members/$', 'games.api.chapter_member_list', name='chapter_member_list'),
    url(r'^api/chapters/(?P<pk>\d+)/members/(?P<slug>[a-z0-9-]+)/$', 'games.api.chapter_member_detail', name='chapter_member_detail'),

    # Users
    url(r'^api/users/register/$', 'users.api.user_registration', name='user_registration'),
    url(r'^api/users/profile/$', 'users.api.user_profile', name='user_profile'),

    url(r'^api/users/(?P<slug>[a-z0-9-]+)/dossier/$', 'dossiers.api.dossier_detail_user', name='user_dossier'),
    url(r'^api/users/(?P<slug>[a-z0-9-]+)/roles/$', 'dossiers.api.user_role_list', name='user_dossier'),
    url(r'^api/users/(?P<slug>[a-z0-9-]+)/roles/(?P<pk>\d+)/$', 'dossiers.api.user_role_detail', name='user_dossier'),
    url(r'^api/users/(?P<slug>[a-z0-9-]+)/awards/$', 'awards.api.user_award_list', name='user_dossier'),
    url(r'^api/users/(?P<slug>[a-z0-9-]+)/awards/(?P<pk>\d+)/$', 'awards.api.user_award_detail', name='user_dossier'),
    url(r'^api/users/(?P<slug>[a-z0-9-]+)/issues/$', 'dossiers.api.issue_list', name='user_issues'),
    url(r'^api/users/(?P<slug>[a-z0-9-]+)/issues/(?P<pk>\d+)/$', 'dossiers.api.issue_detail', name='user_issue'),

    url(r'^api/ranks/$', 'users.api.rank_list', name='rank_list'),
    url(r'^api/ranks/(?P<slug>[a-z0-9-]+)/$', 'users.api.rank_detail', name='rank_detail'),

    # Dossiers
    url(r'^api/dossiers/$', 'dossiers.api.dossier_list', name='dossier_notes'),
    url(r'^api/dossiers/(?P<slug>[a-z0-9-]+)/$', 'dossiers.api.dossier_detail', name='nonuser_dossier'),
    url(r'^api/dossiers/(?P<slug>[a-z0-9-]+)/notes/$', 'dossiers.api.note_list', name='dossier_notes'),
    url(r'^api/dossiers/(?P<slug>[a-z0-9-]+)/notes/(?P<pk>\d+)/$', 'dossiers.api.note_detail', name='dossier_notes_detail'),
    url(r'^api/dossiers/(?P<slug>[a-z0-9-]+)/roles/$', 'dossiers.api.dossier_role_list', name='dossier_roles_list'),
    url(r'^api/dossiers/(?P<slug>[a-z0-9-]+)/roles/(?P<pk>\d+)/$', 'dossiers.api.dossier_role_detail', name='dossier_roles_detail'),
    url(r'^api/headings/$', 'dossiers.api.heading_list', name='dossier_heading_list'),
    url(r'^api/headings/(?P<pk>\d+)/$', 'dossiers.api.heading_detail', name='dossier_heading_detail'),

    # Activity Feed
    url(r'^api/feed-posts/$', 'activityfeed.api.feed_post_list', name='feed_item_post'),
    url(r'^api/feed/$', 'activityfeed.api.feed_item_list', name='feed_item_list'),
    url(r'^api/feed/(?P<pk>\d+)/$', 'activityfeed.api.feed_item_detail', name='feed_item_detail'),

    url(r'^api/notifications/$', 'notifications.api.notification_list', name='notification_list'),

    # Polls
    url(r'^api/polls/$', 'polls.api.poll_list', name='poll_list'),
    url(r'^api/polls/(?P<slug>[a-z0-9-]+)/$', 'polls.api.poll_detail', name='poll_detail'),
    url(r'^api/polls/(?P<slug>[a-z0-9-]+)/choices/$', 'polls.api.item_list', name='item_list'),
    url(r'^api/polls/(?P<slug>[a-z0-9-]+)/choices/(?P<pk>\d+)/$', 'polls.api.item_detail', name='item_detail'),
    url(r'^api/polls/(?P<slug>[a-z0-9-]+)/votes/$', 'polls.api.vote_list', name='vote_list'),
    url(r'^api/polls/(?P<slug>[a-z0-9-]+)/votes/(?P<pk>\d+)/$', 'polls.api.vote_detail', name='vote_detail'),

    # Multimedia
    url(r'^api/screenshots/$', 'multimedia.api.screenshot_list', name='screenshot_list'),
    url(r'^api/screenshots/(?P<slug>[a-z0-9-]+)/$', 'multimedia.api.screenshot_detail', name='screenshot_detail'),
    url(r'^api/quotes/$', 'multimedia.api.quote_list', name='quote_list'),
    url(r'^api/quotes/(?P<slug>[a-z0-9-]+)/$', 'multimedia.api.quote_detail', name='quote_detail'),

    # Publications
    url(r'^api/news/$', 'publications.api.news_list', name='news_list'),
    url(r'^api/news/(?P<slug>[a-z0-9-]+)/$', 'publications.api.news_detail', name='news_detail'),

    url(r'^api/news/(?P<slug>[a-z0-9-]+)/comments/$', 'publications.api.news_comment_list', name='news_comments_list'),
    url(r'^api/news/(?P<slug>[a-z0-9-]+)/comments/(?P<pk>\d+)/$', 'publications.api.news_comment_detail', name='news_comments_detail'),

    url(r'^api/codex/(?P<slug>[a-z0-9-]+)/comments/$', 'publications.api.codex_comment_list', name='codex_comments_list'),
    url(r'^api/codex/(?P<slug>[a-z0-9-]+)/comments/(?P<pk>\d+)/$', 'publications.api.codex_comment_detail', name='codex_comments_detail'),

    url(r'^api/articles/$', 'publications.api.article_list', name='article_list'),
    url(r'^api/articles/(?P<slug>[a-z0-9-]+)/$', 'publications.api.article_detail', name='article_detail'),

    url(r'^api/articles/(?P<slug>[a-z0-9-]+)/comments/$', 'publications.api.article_comment_list', name='article_comments_list'),
    url(r'^api/articles/(?P<slug>[a-z0-9-]+)/comments/(?P<pk>\d+)/$', 'publications.api.article_comment_detail', name='article_comments_detail'),

    url(r'^api/codex/$', 'publications.api.codex_list', name='codex_list'),
    url(r'^api/codex/(?P<pk>\d+)/$', 'publications.api.codex_detail', name='codex_detail'),

    url(r'^verify/(?P<key>[A-Za-z0-9]{32})/$', 'users.views.verify_email', name='verify_email'),
    )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns += patterns('',
#                         url(r'^.*$', 'frontend.views.index', name='catchall')
#                         )
