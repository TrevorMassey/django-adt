# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0004_auto_20150601_0400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='awardcategory',
            options={'ordering': ('-id',), 'verbose_name': 'award category', 'verbose_name_plural': 'award categories'},
        ),
    ]
