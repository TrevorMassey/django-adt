import logging
from django.core.files import File
import os

import django_adt
from django.core.management.base import BaseCommand, CommandError
from users.models import Rank

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args, **options):
        # do some stuff

        self.stdout.write("Jmerlin is a fgt.")

        self.load_ranks()

    def load_ranks(self):

        current_dir = os.path.dirname(os.path.realpath(__file__))
        image_dir = os.path.join(current_dir, '../../static/img/ranks/')

        RANKS = [
            {
                'title': 'Fodder',
                'order': 1,
                'image_file': '00-Fodder.png',
                'description': 'Rank assigned to new recruits undergoing their 2 week trial period.',
                'color': '666666',
            },
            {
                'title': 'Private',
                'order': 2,
                'image_file': '01-Private.png',
                'description': 'Full Member of Addiction.',
                'color': '006633',
            },
            {
                'title': 'Private First Class',
                'order': 3,
                'image_file': '02-Private-First-Class.png',
                'description': 'Six Months service to Addiction.',
                'color': '006633',
            },
            {
                'title': 'Lance Corporal',
                'order': 4,
                'image_file': '03-Lance-Corporal.png',
                'description': 'One year service to Addiction.',
                'color': '006633',
            },
            {
                'title': 'Corporal',
                'order': 5,
                'image_file': '04-Corporal.png',
                'description': 'Two years service to Addiction.',
                'color': '006633',
            },
            {
                'title': 'Sergeant',
                'order': 6,
                'image_file': '05-Sergeant.png',
                'description': 'Distinguished Members.',
                'color': '006633',
            },
            {
                'title': 'Staff Sergeant',
                'order': 7,
                'image_file': '06-Staff-Sergeant.png',
                'description': 'Non-Commissioned Officers.',
                'color': '990000',
            },
            {
                'title': 'Sergeant First Class',
                'order': 8,
                'image_file': '07-Sergeant-First-Class.png',
                'description': 'Non-Commissioned Officers.',
                'color': '990000',
            },
            {
                'title': 'Master Sergeant',
                'order': 9,
                'image_file': '08-Master-Sergeant.png',
                'description': 'Non-Commissioned Officers.',
                'color': '990000',
            },
            {
                'title': 'Sergeant Major',
                'order': 10,
                'image_file': '09-Sergeant-Major.png',
                'description': 'Non-Commissioned Officers.',
                'color': '990000',
            },
            {
                'title': 'Warrant Officer',
                'order': 11,
                'image_file': '10-Warrant-Officer.png',
                'description': 'Specialized Roles.',
                'color': '660099',
            },
            {
                'title': '2nd Lieutenant',
                'order': 12,
                'image_file': '11-2nd-Lieutenant.png',
                'description': 'Officer in Training/Junior Officer.',
                'color': '003399',
            },
            {
                'title': '1st Lieutenant',
                'order': 13,
                'image_file': '12-1st-Lieutenant.png',
                'description': 'Junior Officer. Direct Leadership.',
                'color': '003399',
            },
            {
                'title': 'Captain',
                'order': 14,
                'image_file': '13-Captain.png',
                'description': 'Junior Officer. Indirect Leadership.',
                'color': '003399',
            },
            {
                'title': 'Major',
                'order': 15,
                'image_file': '14-Major.png',
                'description': 'Senior Officer, Division Head, Indirect Leadership.',
                'color': '003399',
            },
            {
                'title': 'Lieutenant Colonel',
                'order': 16,
                'image_file': '15-Lieutenant-Colonel.png',
                'description': 'Senior Officer, Section Executive Officer, Indirect Leadership.',
                'color': '003399',
            },
            {
                'title': 'Colonel',
                'order': 17,
                'image_file': '16-Colonel.png',
                'description': 'Senior Officer, Section Leader, Indirect Leadership.',
                'color': '003399',
            },
            {
                'title': 'Commander',
                'order': 18,
                'image_file': '17-Commander.png',
                'description': 'Executive Staff, Admiralty Board, Executive Leadership.',
                'color': 'ffd700',
            },
            {
                'title': 'Commodore',
                'order': 19,
                'image_file': '18-Commodore.png',
                'description': 'Executive Staff, Addiction Executive Officer.',
                'color': 'ffd700',
            },
            {
                'title': 'Arbiter',
                'order': 20,
                'image_file': '19-Arbiter.png',
                'description': 'Executive Staff, Head of Addiction.',
                'color': 'ffd700',
            },
        ]

        for rank_data in RANKS:
            try:
                rank = Rank.objects.get(title=rank_data.get('title'))
            except Rank.DoesNotExist:
                rank = Rank()
                rank.title = rank_data.get('title')

            rank.order = rank_data.get('order')
            rank.description = rank_data.get('description')
            rank.color = rank_data.get('color')
            file_path = os.path.abspath(os.path.join(image_dir, rank_data.get('image_file')))

            with open(file_path) as f:
                rank.image = File(f)
                rank.save()
