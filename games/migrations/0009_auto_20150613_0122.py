# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_auto_20150605_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapterrole',
            name='division',
        ),
        migrations.RemoveField(
            model_name='chapterrole',
            name='member',
        ),
        migrations.DeleteModel(
            name='ChapterRole',
        ),
        migrations.AddField(
            model_name='chaptermember',
            name='division',
            field=models.ForeignKey(related_name='members', blank=True, to='games.ChapterDivision', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chaptermember',
            name='role',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
