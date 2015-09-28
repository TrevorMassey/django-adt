# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dkp', '0010_transaction_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='section',
            field=models.ForeignKey(related_name='transactions', default=1, to='dkp.Section'),
            preserve_default=False,
        ),
    ]
