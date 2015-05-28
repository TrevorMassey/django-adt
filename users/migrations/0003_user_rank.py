# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150527_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.OneToOneField(null=True, blank=True, to='users.Rank'),
            preserve_default=True,
        ),
    ]
