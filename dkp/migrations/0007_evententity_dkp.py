# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dkp', '0006_auto_20150627_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='evententity',
            name='dkp',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
