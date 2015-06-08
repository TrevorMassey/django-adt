# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_auto_20150601_0411'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codex',
            options={'ordering': ('-created',), 'verbose_name': 'codex', 'verbose_name_plural': 'codex'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-id',), 'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
    ]
