import logging
from django.test import TestCase
from users.online import OnlineUserSource

from users.online.redis_user_manager import RedisUserManager
from swampdragon.pubsub_providers.redis_publisher import get_redis_cli

logger = logging.getLogger(__name__)

class TestOnlineUsers(TestCase):

    def setUp(self):
        self.rum = RedisUserManager()
        self.redis = get_redis_cli()
        self.cleanup_online_users()

    def cleanup_online_users(self):
        self.redis.zremrangebyscore(self.rum.online_user_set_name, min='-inf', max='+inf')

    def get_online_users(self):
        online_users = self.redis.zrangebyscore(self.rum.online_user_set_name, 0, 9001, withscores=True)
        return online_users

    def test_add_online_user_on_website(self):

        self.rum.add_user(1, website_location='/forum')
        self.assertEqual(len(self.rum.get_users()), 1)

        self.rum.add_user(2, website_location='/forum')
        self.assertEqual(len(self.rum.get_users()), 2)

    def test_add_online_user_multiple_locations(self):

        self.rum.add_user(1, website_location='/forum')
        self.rum.add_user(1, website_location='/r/spacedicks')
        self.rum.add_user(1, website_location='/codex/some-slug')
        self.rum.add_user(1, ts_location='starcitiwin')

        online_users = self.rum.get_users(withscores=True)

        self.assertEqual(len(online_users), 1)

        user, score = online_users[0]

        self.assertEqual(score, 4)

    def test_user_go_offline(self):
        self.rum.add_user(1, website_location='/whocares')
        self.rum.add_user(1, ts_location='StarCitiwin')

        self.assertEqual(len(self.rum.get_users()), 1)
        self.rum.decrement_user(1, source=OnlineUserSource.WEBSITE)
        self.assertEqual(len(self.rum.get_users()), 1)
        self.rum.decrement_user(1, source=OnlineUserSource.TEAMSPEAK)
        self.assertEqual(len(self.rum.get_users()), 0)
