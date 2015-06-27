from django.apps.config import AppConfig

class DkpConfig(AppConfig):
    name = 'dkp'
    verbose_name = 'dkp'

    def ready(self):
        import dkp.signals

default_app_config = 'dkp.DkpConfig'
