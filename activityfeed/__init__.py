from django.apps.config import AppConfig


class ActivityFeedConfig(AppConfig):
    name = 'activityfeed'
    verbose_name = 'Activity Feed'

    def ready(self):
        import activityfeed.signals

default_app_config = 'activityfeed.ActivityFeedConfig'
