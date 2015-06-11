# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0008_auto_20150609_2255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codex',
            options={'ordering': ('-created',), 'verbose_name': 'codex', 'verbose_name_plural': 'codex'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='body_clean',
        ),
    ]
