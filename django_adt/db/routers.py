__author__ = 'Alex'

class LegacyDBRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    ADDICT_FORUM = 'addict_forum'
    ADDICT_WEBSITE = 'addict_website'
    ADDICT_LOGS = 'addict_logs'

    LEGACY_APPS = (
        ADDICT_FORUM,
        ADDICT_WEBSITE,
        ADDICT_LOGS,
    )

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == self.ADDICT_WEBSITE:
            return self.ADDICT_WEBSITE
        if model._meta.app_label == self.ADDICT_FORUM:
            return self.ADDICT_FORUM
        if model._meta.app_label == self.ADDICT_LOGS:
            return self.ADDICT_LOGS
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == self.ADDICT_WEBSITE:
            return self.ADDICT_WEBSITE
        if model._meta.app_label == self.ADDICT_FORUM:
            return self.ADDICT_FORUM
        if model._meta.app_label == self.ADDICT_LOGS:
            return self.ADDICT_LOGS
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label in self.LEGACY_APPS or \
           obj2._meta.app_label in self.LEGACY_APPS:
           return False
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label in self.LEGACY_APPS:
            return False
        return None