# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dossiers', '0003_auto_20150527_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='application',
            field=models.ForeignKey(blank=True, to='applications.Application', null=True),
            preserve_default=True,
        ),
    ]
