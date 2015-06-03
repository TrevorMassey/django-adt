# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activityfeed', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feeditem',
            options={'permissions': (('soft_delete_feeditem', 'Can soft delete feed item'),)},
        ),
    ]
