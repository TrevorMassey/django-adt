from swampdragon.pubsub_providers.data_publisher import publish_data
from swampdragon.pubsub_providers.redis_publisher import get_redis_cli
from users.online import OnlineUserSource
__author__ = 'Alex'


class RedisUserManager(object):

    redis_cli = None

    online_user_set_name = 'online_users'

    def __init__(self):
        self.redis_cli = get_redis_cli()

    def add_user(self, id, website_location=None, ts_location=None):
        self.redis_cli.zincrby(name=self.online_user_set_name, value=id, amount=1)

    def decrement_user(self, id, source):

        if source not in OnlineUserSource.ALL_SOURCES:
            raise ValueError("Online users source must be one of %s" % (OnlineUserSource.ALL_SOURCES,))

        if source == OnlineUserSource.WEBSITE:
            # Clear user website location from HSET
            pass
        elif source == OnlineUserSource.TEAMSPEAK:
            # Clear user ts location from HSET
            pass

        self.redis_cli.zincrby(self.online_user_set_name, id, amount=-1)

    def get_users(self, exclude_ids=None, withscores=False):
        return self.redis_cli.zrangebyscore(self.online_user_set_name, min=1, max=9001, withscores=withscores)

    def publish_online_users(self):
        data = {
            'users_online': self.get_users()
        }

        publish_data(channel='online_users', data=data)

    def cleanup(self):

        self.redis_cli.zremrangebyscore(self.online_user_set_name, min='-inf', max=0)
