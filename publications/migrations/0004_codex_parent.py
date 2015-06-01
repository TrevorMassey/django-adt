# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_auto_20150601_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='codex',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='publications.Codex', null=True),
            preserve_default=True,
        ),
    ]
