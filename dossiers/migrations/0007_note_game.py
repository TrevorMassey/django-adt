# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_chapterdivision_chapter'),
        ('dossiers', '0006_auto_20150612_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='game',
            field=models.ForeignKey(related_name='+', default=1, to='games.Game'),
            preserve_default=False,
        ),
    ]
