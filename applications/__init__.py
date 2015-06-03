from django.apps.config import AppConfig


class ApplicationsConfig(AppConfig):
    name = 'applications'
    verbose_name = 'Applications'

    def ready(self):
        pass

default_app_config = 'applications.ApplicationsConfig'
