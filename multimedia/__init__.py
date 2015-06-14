from django.apps.config import AppConfig


class MultimediaConfig(AppConfig):
    name = 'multimedia'
    verbose_name = 'Multimedia'

    def ready(self):
        import multimedia.signals

default_app_config = 'multimedia.MultimediaConfig'