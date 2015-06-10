# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0005_auto_20150609_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='views',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
