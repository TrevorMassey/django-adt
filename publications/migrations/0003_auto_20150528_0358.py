# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=b'title', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='codex',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=b'title', editable=False, blank=True),
            preserve_default=True,
        ),
    ]
