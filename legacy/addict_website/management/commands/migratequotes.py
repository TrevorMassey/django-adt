from datetime import datetime
import logging
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.utils import timezone
from multimedia.models import Quote

from legacy.addict_website.models import Quotes as LegacyQuote


logger = logging.getLogger(__name__)

class Command(BaseCommand):


    def handle(self, *args, **options):
        self.migrate_quotes()

    def migrate_quotes(self):
        Quote.objects.all().delete()
        for legacy_quote in LegacyQuote.objects.all():
            assert isinstance(legacy_quote, LegacyQuote)

            date_naive = datetime.utcfromtimestamp(legacy_quote.posted)
            date = timezone.make_aware(date_naive, timezone.utc)

            quote = Quote()
            quote.title = legacy_quote.title
            quote.body = legacy_quote.quote
            quote.created = date
            quote.type = 'internal'

            #quote.image - blob field?

            quote.poster_id = legacy_quote.poster

            quote.save()
