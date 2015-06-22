# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0010_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=b'title', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
