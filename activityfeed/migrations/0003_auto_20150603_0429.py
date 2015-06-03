# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0004_auto_20150601_0400'),
        ('activityfeed', '0002_auto_20150603_0355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeditem',
            name='award_recipient',
        ),
        migrations.AddField(
            model_name='feeditem',
            name='award',
            field=models.ForeignKey(blank=True, to='awards.Award', null=True),
            preserve_default=True,
        ),
    ]
