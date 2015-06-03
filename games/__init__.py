from django.apps.config import AppConfig


class GamesConfig(AppConfig):
    name = 'games'
    verbose_name = 'Games'

    def ready(self):
        import games.signals

default_app_config = 'games.GamesConfig'
