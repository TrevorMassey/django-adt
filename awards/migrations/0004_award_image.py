# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_auto_20150527_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='image',
            field=models.ForeignKey(default=1, to='awards.AwardImage'),
            preserve_default=False,
        ),
    ]
