# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150602_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rank',
            name='users',
        ),
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.ForeignKey(related_name='users', blank=True, to='users.Rank', null=True),
            preserve_default=True,
        ),
    ]
