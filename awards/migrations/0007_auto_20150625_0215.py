# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0006_auto_20150625_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardrecipient',
            name='reason',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
