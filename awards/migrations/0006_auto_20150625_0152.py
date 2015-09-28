# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_auto_20150608_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardcategory',
            name='chapter',
            field=models.ForeignKey(related_name='award_categories', blank=True, to='games.Chapter', null=True),
            preserve_default=True,
        ),
    ]
