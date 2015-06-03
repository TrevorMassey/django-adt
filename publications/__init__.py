from django.apps.config import AppConfig


class PublicationsConfig(AppConfig):
    name = 'publications'
    verbose_name = 'Publications'

    def ready(self):
        import publications.signals

default_app_config = 'publications.PublicationsConfig'
