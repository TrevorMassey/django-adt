# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150601_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rank',
            name='number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rank',
        ),
        migrations.AddField(
            model_name='rank',
            name='order',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rank',
            name='users',
            field=models.ForeignKey(related_name='rank', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
