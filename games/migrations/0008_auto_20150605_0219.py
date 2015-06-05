# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20150605_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterrole',
            name='division',
            field=models.ForeignKey(related_name='members', to='games.ChapterDivision'),
            preserve_default=True,
        ),
    ]
