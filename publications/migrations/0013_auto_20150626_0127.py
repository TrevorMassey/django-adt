# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0012_auto_20150614_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(related_name='articles', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
