# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20150608_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
