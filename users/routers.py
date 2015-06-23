import logging
from swampdragon import route_handler

from swampdragon.route_handler import BaseRouter
#from swampdragon_auth.mixins import JsonWebTokenAuthMixin

from users.models import User

logger = logging.getLogger(__name__)

class JsonWebTokenAuthMixin(object):
    def handle(self, data):
        if data['verb'] == 'subscribe' and 'auth' in data['args']:
            jwt = data['args'].pop('auth')
            self.connection.authenticate(jwt)
        super(JsonWebTokenAuthMixin, self).handle(data)

class OnlineUsersRouter(JsonWebTokenAuthMixin, BaseRouter):
    route_name = 'online-users'
    valid_verbs = ['subscribe', 'unsubscribe', 'get_online_user_list']

    def subscribe(self, **kwargs):
        """
        Only subscribe online users
        """
        logger.info("Subscription to Online User Router")

        logger.info('Context: %s', self.context)
        logger.info('Kwargs: %s', kwargs)

        if not self.connection.user:
            logger.info("no user for connection")
            return

        super(OnlineUsersRouter, self).subscribe(**kwargs)

        if self.connection.user:
            logger.info("User %s online: %s", self.connection.user.id, self.connection.user)
            # user_manager.add_user(self.connection.user.pk)
        else:
            logger.info("No User")

    def unsubscribe(self, **kwargs):
        logger.info("User disconnect: %s", self.connection.user)

    def get_subscription_channels(self, **kwargs):
        return ['online_users']

    def get_online_user_list(self, **kwargs):
        self.send({'online': ['a', 'b', 'c']})

route_handler.register(OnlineUsersRouter)
