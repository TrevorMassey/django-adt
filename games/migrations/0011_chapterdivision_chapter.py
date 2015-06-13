# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_auto_20150613_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapterdivision',
            name='chapter',
            field=models.ForeignKey(related_name='divisions', default=3, to='games.Chapter'),
            preserve_default=False,
        ),
    ]
