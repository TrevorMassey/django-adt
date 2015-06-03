# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_chapter_creator'),
        ('applications', '0004_application_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='chapter',
            field=models.ForeignKey(default=1, to='games.Chapter'),
            preserve_default=False,
        ),
    ]
