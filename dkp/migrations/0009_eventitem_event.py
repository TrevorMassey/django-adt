# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dkp', '0008_auto_20150627_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventitem',
            name='event',
            field=models.ForeignKey(related_name='awarded_items', default=1, to='dkp.Event'),
            preserve_default=False,
        ),
    ]
