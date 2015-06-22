# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activityfeed', '0009_auto_20150614_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeditem',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
