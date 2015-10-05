# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='posts',
            new_name='post_count',
        ),
        migrations.RenameField(
            model_name='forum',
            old_name='topics',
            new_name='topic_count',
        ),
        migrations.AlterField(
            model_name='post',
            name='forum',
            field=models.ForeignKey(related_name='posts', to='forums.Forum'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(related_name='posts', to='forums.Topic'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='forum',
            field=models.ForeignKey(related_name='topics', to='forums.Forum'),
            preserve_default=True,
        ),
    ]
