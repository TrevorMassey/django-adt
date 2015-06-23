import logging

from swampdragon import route_handler
from swampdragon.route_handler import BaseRouter

logger = logging.getLogger(__name__)


class ActivityFeedRouter(BaseRouter):
    route_name = 'activityfeed'

    def get_subscription_channels(self, **kwargs):
        channels = ('feed', )

        pk = kwargs.pop('pk')

        if pk:
            channels = ['post-{pk}'.format(pk=pk)]
            channels.append('feed')

        return channels

    def subscribe(self, **kwargs):
        logger.info(kwargs)
        super(ActivityFeedRouter, self).subscribe(**kwargs)


route_handler.register(ActivityFeedRouter)
