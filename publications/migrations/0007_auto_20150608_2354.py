# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0006_auto_20150608_2329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codex',
            options={'ordering': ('-created',)},
        ),
    ]
