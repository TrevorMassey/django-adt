# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_auto_20150601_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='category',
            field=models.ForeignKey(related_name='awards', to='awards.AwardCategory'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awardcategory',
            name='chapter',
            field=models.ForeignKey(related_name='award_categories', to='games.Chapter'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awardrecipient',
            name='award',
            field=models.ForeignKey(related_name='award_recipient', to='awards.Award'),
            preserve_default=True,
        ),
    ]
