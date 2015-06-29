# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dkp', '0005_auto_20150626_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='event',
        ),
        migrations.AddField(
            model_name='resourcecontrib',
            name='dkp',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='bonus',
            field=models.ForeignKey(related_name='+', blank=True, to='dkp.Bonus', null=True),
            preserve_default=True,
        ),
    ]
