from django.apps.config import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = 'Users'

    def ready(self):
        import users.signals

default_app_config = 'users.UsersConfig'
