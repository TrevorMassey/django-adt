# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dkp', '0002_auto_20150626_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='standby_rate',
            field=models.FloatField(default=0.5),
            preserve_default=True,
        ),
    ]
