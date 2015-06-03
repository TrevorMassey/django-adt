from django.apps.config import AppConfig


class AwardsConfig(AppConfig):
    name = 'awards'
    verbose_name = 'Awards'

    def ready(self):
        import awards.signals

default_app_config = 'awards.AwardsConfig'
