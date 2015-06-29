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
                'image_file': '1.png',
                'description': 'Rank assigned to new recruits undergoing their 2 week trial period.',
                'color': '666666',
            },
            {
                'title': 'Private',
                'order': 2,
                'image_file': '2.png',
                'description': 'Full Member of Addiction.',
                'color': '006633',
            },
            {
                'title': 'Private First Class',
                'order': 3,
                'image_file': '3.png',
                'description': 'Six Months service to Addiction.',
                'color': '006633',
            },
            {
                'title': 'Lance Corporal',
                'order': 4,
                'image_file': '4.png',
                'description': 'One year service to Addiction.',
                'color': '006633',
            },
            {
                'title': 'Corporal',
                'order': 5,
                'image_file': '5.png',
                'description': 'Two years service to Addiction.',
                'color': '006633',
            },
            {
                'title': 'Sergeant',
                'order': 6,
                'image_file': '6.png',
                'description': 'Distinguished Members.',
                'color': '006633',
            },
            {
                'title': 'Staff Sergeant',
                'order': 7,
                'image_file': '7.png',
                'description': 'Non-Commissioned Officers.',
                'color': '990000',
            },
            {
                'title': 'Sergeant First Class',
                'order': 8,
                'image_file': '8.png',
                'description': 'Non-Commissioned Officers.',
                'color': '990000',
            },
            {
                'title': 'Master Sergeant',
                'order': 9,
                'image_file': '9.png',
                'description': 'Non-Commissioned Officers.',
                'color': '990000',
            },
            {
                'title': 'Sergeant Major',
                'order': 10,
                'image_file': '10.png',
                'description': 'Non-Commissioned Officers.',
                'color': '990000',
            },
            {
                'title': 'Warrant Officer',
                'order': 11,
                'image_file': '11.png',
                'description': 'Specialized Roles.',
                'color': '660099',
            },
            {
                'title': '2nd Lieutenant',
                'order': 12,
                'image_file': '12.png',
                'description': 'Officer in Training/Junior Officer.',
                'color': '003399',
            },
            {
                'title': '1st Lieutenant',
                'order': 13,
                'image_file': '13.png',
                'description': 'Junior Officer. Direct Leadership.',
                'color': '003399',
            },
            {
                'title': 'Captain',
                'order': 14,
                'image_file': '14.png',
                'description': 'Junior Officer. Indirect Leadership.',
                'color': '003399',
            },
            {
                'title': 'Major',
                'order': 15,
                'image_file': '15.png',
                'description': 'Senior Officer, Division Head, Indirect Leadership.',
                'color': '003399',
            },
            {
                'title': 'Lieutenant Colonel',
                'order': 16,
                'image_file': '16.png',
                'description': 'Senior Officer, Section Executive Officer, Indirect Leadership.',
                'color': '003399',
            },
            {
                'title': 'Colonel',
                'order': 17,
                'image_file': '17.png',
                'description': 'Senior Officer, Section Leader, Indirect Leadership.',
                'color': '003399',
            },
            {
                'title': 'Commander',
                'order': 18,
                'image_file': '18.png',
                'description': 'Executive Staff, Admiralty Board, Executive Leadership.',
                'color': 'ffd700',
            },
            {
                'title': 'Commodore',
                'order': 19,
                'image_file': '19.png',
                'description': 'Executive Staff, Addiction Executive Officer.',
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
