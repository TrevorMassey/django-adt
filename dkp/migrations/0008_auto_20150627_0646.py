# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dkp', '0007_evententity_dkp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='game',
        ),
        migrations.AddField(
            model_name='event',
            name='dkp',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='section',
            field=models.ForeignKey(related_name='+', default=1, to='dkp.Section'),
            preserve_default=False,
        ),
    ]
