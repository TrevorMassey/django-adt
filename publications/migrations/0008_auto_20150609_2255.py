# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0007_auto_20150608_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codex',
            name='order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
