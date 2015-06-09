# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(max_length=30, choices=[(b'username_mention_comment', b'Username Mentioned in Comment'), (b'username_mention_forum', b'Username Mentioned in Forum Post'), (b'application', b'Application Status Change'), (b'award', b'Received Award'), (b'promotion', b'Received Promotion'), (b'demotion', b'Received Demotion'), (b'event', b'New Event'), (b'kicked', b'Kicked from guild'), (b'quote', b'You were quoted'), (b'screenshot', b'You were tagged in a screenshot'), (b'chapter', b'You were added to a chapter')]),
            preserve_default=True,
        ),
    ]
