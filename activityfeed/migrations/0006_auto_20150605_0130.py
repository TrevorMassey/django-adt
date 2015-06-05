# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activityfeed', '0005_auto_20150603_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeditem',
            name='type',
            field=models.CharField(max_length=15, choices=[(b'feed_post', b'New Feed Post'), (b'forum_post', b'New Forum Post'), (b'join_chapter', b'Joined Chapter'), (b'screenshot', b'Uploaded Screenshot'), (b'video', b'New Video'), (b'quote', b'New Quote'), (b'new_chapter', b'New Chapter'), (b'promotion', b'Promoted'), (b'demotion', b'Demoted'), (b'award', b'New Award Recipient'), (b'news', b'New News')]),
            preserve_default=True,
        ),
    ]
