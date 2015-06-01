# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150531_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_key_expires',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='key',
            field=models.CharField(max_length=32, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
