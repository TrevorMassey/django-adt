from datetime import datetime
import logging
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.utils import timezone

from users.models import User
from legacy.addict_website.models import Users as LegacyUser


logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.migrate_users()

    def migrate_users(self):

        new_users = []

        for legacy_user in LegacyUser.objects.all():
            assert isinstance(legacy_user, LegacyUser)

            reg_date_naive = datetime.utcfromtimestamp(legacy_user.regdate)
            reg_date = timezone.make_aware(reg_date_naive, timezone.utc)

            existing_user = User.objects.filter(Q(email=legacy_user.email) | Q(username=legacy_user.username))

            if existing_user:
                self.stdout.write("Duplicate user for id {id}".format(id=legacy_user.record))
                continue

            user = User()
            user.id = legacy_user.record
            user.email = legacy_user.email
            user.username = legacy_user.username
            user.display_name = legacy_user.username
            user.date_joined = reg_date
            user.ts_uid = legacy_user.tsuid
            user.save()

