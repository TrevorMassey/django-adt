# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dossiers', '0002_auto_20150527_0416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guild',
            name='game',
        ),
        migrations.AlterField(
            model_name='guild',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=b'title', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='role',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=b'role', editable=False, blank=True),
            preserve_default=True,
        ),
    ]
